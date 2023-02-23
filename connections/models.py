from django.db import models
from django.db.models import Max
# Create your models here.

class ConnectionUnitType(models.Model):
    name = models.CharField('Наименование', max_length=16, unique=True)

    class Meta:
        verbose_name = "Тип интерфейса"
        verbose_name_plural = "Типы интерфейсов"

    def __str__(self):
        return self.name


def autoincrement():
    last = ConnectionUnit.objects.all().aggregate(max=Max('number'))
    return last['max'] + 1 if last['max'] else 1


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
        default=autoincrement
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

    class Meta:
        verbose_name = "Интерфейс"
        verbose_name_plural = "Интерфейсы"

    def __str__(self):
        return f'{self.type} № {self.number}'
