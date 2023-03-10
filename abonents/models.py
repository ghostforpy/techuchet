from django.db import models
from django.urls import reverse
# Create your models here.

class ObjectStatus(models.Model):
    name = models.CharField('Наименование', max_length=50, unique=True)

    class Meta:
        verbose_name = "Статус объекта"
        verbose_name_plural = "Статусы объектов"
        ordering = ['id']

    def __str__(self):
        return self.name

class AbonentType(models.Model):
    name = models.CharField('Наименование', max_length=16, unique=True)

    class Meta:
        verbose_name = "Тип абонента"
        verbose_name_plural = "Типы абонентов"
        ordering = ['id']

    def __str__(self):
        return self.name

class Abonent(models.Model):
    name = models.CharField('Имя', max_length=25, unique=True)
    type = models.ForeignKey(AbonentType, on_delete=models.CASCADE, verbose_name="Тип")
    created_date = models.DateField('Дата создания', auto_now_add=True)
    change_date = models.DateField('Дата изменения', auto_now=True)
    enable_date = models.DateField('Дата подключения', blank=True, null=True)
    disable_date = models.DateField('Дата отключения', blank=True, null=True)
    phone = models.CharField('Номер телефона', max_length=30, unique=True, null=True, blank=True)
    contract = models.CharField('Номер договора', max_length=50, unique=True, null=True, blank=True)
    object_status = models.ForeignKey(
        ObjectStatus,
        on_delete=models.CASCADE,
        verbose_name='Статус',
        blank=True,
        null=True
    )
    building = models.ForeignKey(
        'buildings.building',
        on_delete=models.CASCADE,
        verbose_name="Здание",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Абонент"
        verbose_name_plural = "Абоненты"
        ordering = ['id']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('abonent-detail', kwargs={'pk': self.pk})