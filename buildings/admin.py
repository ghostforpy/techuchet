from django.contrib import admin

# Register your models here.
from .models import Building, BuildingType


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    pass


@admin.register(BuildingType)
class BuildingTypeAdmin(admin.ModelAdmin):
    pass