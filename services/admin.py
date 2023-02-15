from django.contrib import admin

# Register your models here.
from .models import Service, ServiceType


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass


@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    pass