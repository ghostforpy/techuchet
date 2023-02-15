from django.db import models

# Create your models here.

class NodeType(models.Model):
    name = models.CharField('Наименование', max_length=16, unique=True)

    class Meta:
        verbose_name = "Тип оборудования"
        verbose_name_plural = "Типы оборудования"


class Node(models.Model):
    type = models.ForeignKey(NodeType, on_delete=models.CASCADE, verbose_name="Тип")
    created_date = models.DateField('Дата создания', auto_created=True)
    change_date = models.DateField('Дата изменения', auto_now_add=True)
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

    class Meta:
        verbose_name = "Логическое устройство"
        verbose_name_plural = "Логические устройства"