from django.db import models
from django.urls import reverse


class NodeType(models.Model):
    name = models.CharField('Наименование', max_length=16, unique=True)

    class Meta:
        verbose_name = "Тип оборудования"
        verbose_name_plural = "Типы оборудования"
        ordering = ['id']

    def __str__(self):
        return self.name


class NodeName(models.Model):
    name = models.CharField('Наименование', max_length=16, unique=True)
    type = models.ForeignKey(
        NodeType, 
        on_delete=models.CASCADE, 
        verbose_name="Тип",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Имя оборудования"
        verbose_name_plural = "Имена оборудования"
        ordering = ['id']

    def __str__(self):
        return self.name


class Node(models.Model):
    name = models.ForeignKey(
        NodeName, 
        on_delete=models.CASCADE, 
        verbose_name="Наименование",
        null=True,
        blank=True
    )
    type = models.ForeignKey(NodeType, on_delete=models.CASCADE, verbose_name="Тип")
    created_date = models.DateField('Дата создания', auto_now_add=True)
    change_date = models.DateField('Дата изменения', auto_now=True)
    entity = models.ForeignKey(
        "entities.entity",
        on_delete=models.CASCADE, 
        verbose_name="Сущность",
        null=True,
        blank=True
    )
    status = models.ForeignKey(
        'abonents.objectstatus',
        on_delete=models.CASCADE,
        verbose_name="Статус",
        null=True,
        blank=True
    )
    building = models.ForeignKey(
        'buildings.building',
        on_delete=models.CASCADE,
        verbose_name="Здание",
        null=True,
        blank=True
    )
    ip_address = models.GenericIPAddressField("IP адрес", null=True, blank=True)
    parent = models.ForeignKey('self', models.CASCADE, null=True, blank=True, verbose_name='Родительское устройство')

    class Meta:
        verbose_name = "Логическое устройство"
        verbose_name_plural = "Логические устройства"
        ordering = ['id']

    def get_absolute_url(self):
        return reverse('node-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.name.name} {self.ip_address}'