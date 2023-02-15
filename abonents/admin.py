from django.contrib import admin

# Register your models here.
from .models import Abonent, AbonentType, ObjectStatus


@admin.register(Abonent)
class AbonentAdmin(admin.ModelAdmin):
    pass


@admin.register(AbonentType)
class AbonentTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(ObjectStatus)
class ObjectStatusAdmin(admin.ModelAdmin):
    pass