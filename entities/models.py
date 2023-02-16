from django.db import models

# Create your models here.

class Entity(models.Model):
    name = models.CharField('Наименование', max_length=25, unique=True)
    table = models.CharField('Таблица', max_length=25, unique=True)

    class Meta:
        verbose_name = "Сущность"
        verbose_name_plural = "Сущности"

    def __str__(self):
        return self.name