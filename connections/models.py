from django.db import models

# Create your models here.

class ConnectionUnitType(models.Model):
    name = models.CharField('Наименование', max_length=16, unique=True)

    class Meta:
        verbose_name = "Тип интерфейса"
        verbose_name_plural = "Типы интерфейсов"

    def __str__(self):
        return self.name

class ConnectionUnit(models.Model):
    type = models.ForeignKey(ConnectionUnitType, on_delete=models.CASCADE, verbose_name="Тип")
    status = models.ForeignKey(
        'abonents.objectstatus',
        on_delete=models.CASCADE,
        verbose_name="Статус",
        null=True,
        blank=True
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
    class Meta:
        verbose_name = "Интерфейс"
        verbose_name_plural = "Интерфейсы"
