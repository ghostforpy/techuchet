from django.contrib import admin

# Register your models here.
from .models import Entity

@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    pass