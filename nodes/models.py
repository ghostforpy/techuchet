from django.db import models
from django.urls import reverse

# Create your models here.

class NodeType(models.Model):
    name = models.CharField('Наименование', max_length=16, unique=True)

    class Meta:
        verbose_name = "Тип оборудования"
        verbose_name_plural = "Типы оборудования"

    def __str__(self):
        return self.name

class Node(models.Model):
    name = models.CharField(
        'Наименование',
        unique=True,
        max_length=25, 
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
    buiilding = models.ForeignKey(
        'buildings.building',
        on_delete=models.CASCADE,
        verbose_name="Здание",
        null=True,
        blank=True
    )
    ip_address = models.GenericIPAddressField("IP адрес", null=True, blank=True)
    parent = models.ForeignKey('self', models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Логическое устройство"
        verbose_name_plural = "Логические устройства"

    def get_absolute_url(self):
        return reverse('node-detail', kwargs={'pk': self.pk})