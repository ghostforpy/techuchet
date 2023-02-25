from django.contrib import admin

# Register your models here.
from .models import Building, BuildingType, RegionType, Region


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    pass


@admin.register(BuildingType)
class BuildingTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(RegionType)
class RegionTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    pass