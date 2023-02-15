from django.db import models

# Create your models here.


class ServiceType(models.Model):
    name = models.CharField('Наименование', max_length=16, unique=True)

    class Meta:
        verbose_name = "Тип сервиса"
        verbose_name_plural = "Типы сервисов"


class Service(models.Model):
    name = models.CharField('Наименование', max_length=25, unique=True)
    type = models.ForeignKey(ServiceType, on_delete=models.CASCADE, verbose_name="Тип")
    created_date = models.DateField('Дата создания', auto_created=True)
    abonent = models.ForeignKey(
        'abonents.Abonent',
        on_delete=models.CASCADE,
        verbose_name='Абонент',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Сервис"
        verbose_name_plural = "Сервисы"