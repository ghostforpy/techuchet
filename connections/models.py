from django.db import models
# from django.db.models import Max
from django.urls import reverse
from django.core.exceptions import ValidationError

# Create your models here.

class ConnectionUnitType(models.Model):
    name = models.CharField('Наименование', max_length=16, unique=True)

    class Meta:
        verbose_name = "Тип интерфейса"
        verbose_name_plural = "Типы интерфейсов"
        ordering = ['id']

    def __str__(self):
        return self.name


# def autoincrement():
    # last = ConnectionUnit.objects.all().aggregate(max=Max('number'))
    # return last['max'] + 1 if last['max'] else 1

class ConnectionUnit(models.Model):
    type = models.ForeignKey(ConnectionUnitType, on_delete=models.CASCADE, verbose_name="Тип")
    status = models.ForeignKey(
        'abonents.objectstatus',
        on_delete=models.CASCADE,
        verbose_name="Статус",
        null=True,
        blank=True
    )
    number = models.IntegerField(
        'Порядковый номер интерфейса',
        blank=True, 
        null=True,
        default=1
    )
    node = models.ForeignKey(
        'nodes.Node',
        on_delete=models.CASCADE,
        verbose_name="Логическое устройство",
        null=True,
        blank=True
    )
    service = models.ForeignKey(
        'services.service',
        on_delete=models.CASCADE,
        verbose_name="Сервис",
        null=True,
        blank=True
    )
    rate = models.FloatField('Пропускная способность', null=True, blank=True)
    entity = models.ForeignKey(
        "entities.entity",
        on_delete=models.CASCADE, 
        verbose_name="Сущность",
        null=True,
        blank=True
    )
    parent_node_connection_unit = models.OneToOneField(
        "self",
        on_delete=models.SET_NULL,
        verbose_name="Порт родительского логического устройства",
        null=True,
        blank=True,
        related_name="children_node_connection_unit"
    )
    in_use_between_nodes = models.BooleanField("Используется для соединения оборудования", default=False)

    class Meta:
        verbose_name = "Интерфейс"
        verbose_name_plural = "Интерфейсы"
        ordering = ['id']

    def __str__(self):
        return f'{self.type} № {self.number} {self.node.ip_address}'

    def get_absolute_url(self):
        return reverse('connection-detail', kwargs={'pk': self.pk})

    def clean(self):
        if self.parent_node_connection_unit and self.service:
            raise ValidationError('Порт не может использоваться для предоставления услуг и для подключения логических устройств одновременно.')
        if self.parent_node_connection_unit:
            if self.node.connectionunit_set.filter(parent_node_connection_unit__isnull=False).exclude(pk=self.pk).exists():
                conn = self.node.connectionunit_set.filter(parent_node_connection_unit__isnull=False).first()
                ip = conn.parent_node_connection_unit.node.ip_address
                msg = f'У данного логического устройства уже выбрано родительское логическое устройство {ip}.'
                raise ValidationError({'parent_node_connection_unit': msg})
            if self.node == self.parent_node_connection_unit.node:
                raise ValidationError({'parent_node_connection_unit':'Нельзя соединять логическое устройство с самим собой.'})
            if self.node.parent != self.parent_node_connection_unit.node:
                msg = f'Выбрано неправильное родительское логическое устройство. Необходимо выбрать порт логического устройства {self.node.parent.ip_address}'
                raise ValidationError({'parent_node_connection_unit': msg})
            if self.parent_node_connection_unit.in_use_between_nodes or self.parent_node_connection_unit.service:
                raise ValidationError({'parent_node_connection_unit':'Порт в родительском логическом устройстве занят.'})

    def save(self, *args, **kwargs):
        self.in_use_between_nodes = self.parent_node_connection_unit is not None or hasattr(self, 'children_node_connection_unit')
        if self.parent_node_connection_unit:
            # установить соединение с родительским устройством
            if not self.parent_node_connection_unit.in_use_between_nodes:
                # поменять у родительского утсройства флаг использования для соединений оборудования
                ConnectionUnit.objects.filter(pk=self.parent_node_connection_unit.pk).update(in_use_between_nodes=True)
            if self.pk:
                # проверка на изменения
                obj = ConnectionUnit.objects.get(pk=self.pk)
                if self.parent_node_connection_unit != obj.parent_node_connection_unit and obj.parent_node_connection_unit:
                    # сбросить у родительского устройства флаг использования для соединений оборудования,
                    # если родительское устройство поменялось
                    ConnectionUnit.objects.filter(pk=obj.parent_node_connection_unit.pk).update(in_use_between_nodes=False)
        else:
            # сброс соединения с родительским устройством
            if self.pk:
                # проверка на изменения
                obj = ConnectionUnit.objects.get(pk=self.pk)
                if obj.parent_node_connection_unit:
                    # сбросить у родительского устройства флаг использования для соединений оборудования
                    ConnectionUnit.objects.filter(pk=obj.parent_node_connection_unit.pk).update(in_use_between_nodes=False)
        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.parent_node_connection_unit:
            # сбросить соединение с родительским устройством
            ConnectionUnit.objects.filter(pk=self.parent_node_connection_unit.pk).update(in_use_between_nodes=False)
        if hasattr(self, 'children_node_connection_unit'):
            # сбросить соединение с подчиненным устройством
            ConnectionUnit.objects.filter(pk=self.children_node_connection_unit.pk).update(in_use_between_nodes=False)
        return super().delete(*args, **kwargs)
