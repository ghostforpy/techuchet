from django.db import models

# Create your models here.

class BuildingType(models.Model):
    name = models.CharField('Наименование', max_length=16, unique=True)

    class Meta:
        verbose_name = "Тип здания"
        verbose_name_plural = "Типы зданий"

    def __str__(self):
        return self.name

class Building(models.Model):
    type = models.ForeignKey(BuildingType, on_delete=models.CASCADE, verbose_name="Тип")
    street = models.CharField('Улица', max_length=25, unique=True)
    house = models.CharField('Дом', max_length=8, unique=True)

    class Meta:
        verbose_name = "Здание"
        verbose_name_plural = "Здания"

    def __str__(self):
        return f'{self.street}, {self.house}'