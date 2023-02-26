from django.db import models

# Create your models here.

class RegionType(models.Model):
    name = models.CharField('Наименование', max_length=100, unique=True)
    
    class Meta:
        verbose_name = "Тип региона"
        verbose_name_plural = "Типы регионов"
        ordering = ['id']

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField('Наименование населенного пункта', max_length=50, unique=True)
    type = models.ForeignKey(RegionType, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"
        ordering = ['id']

    def __str__(self):
        return self.name


class BuildingType(models.Model):
    name = models.CharField('Наименование', max_length=16, unique=True)

    class Meta:
        verbose_name = "Тип здания"
        verbose_name_plural = "Типы зданий"
        ordering = ['id']

    def __str__(self):
        return self.name

class Building(models.Model):
    type = models.ForeignKey(BuildingType, on_delete=models.CASCADE, verbose_name="Тип")
    street = models.CharField('Улица', max_length=25, unique=True)
    house = models.CharField('Дом', max_length=8, unique=True)
    region = models.ForeignKey(Region, models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Здание"
        verbose_name_plural = "Здания"
        ordering = ['id']

    def __str__(self):
        return f'{self.street}, {self.house}'