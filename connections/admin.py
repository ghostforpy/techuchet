from django.contrib import admin

# Register your models here.
from .models import ConnectionUnit, ConnectionUnitType

@admin.register(ConnectionUnitType)
class ConnectionUnitTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(ConnectionUnit)
class ConnectionUnitAdmin(admin.ModelAdmin):
    readonly_fields = ('in_use_between_nodes',)
    pass