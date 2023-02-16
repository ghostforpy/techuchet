from django.db import models
from django.urls import reverse

# Create your models here.


class ServiceType(models.Model):
    name = models.CharField('Наименование', max_length=16, unique=True)

    class Meta:
        verbose_name = "Тип сервиса"
        verbose_name_plural = "Типы сервисов"

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField('Наименование', max_length=25, unique=True)
    type = models.ForeignKey(ServiceType, on_delete=models.CASCADE, verbose_name="Тип")
    created_date = models.DateField('Дата создания', auto_now_add=True)
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

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('service-detail', kwargs={'pk': self.pk})