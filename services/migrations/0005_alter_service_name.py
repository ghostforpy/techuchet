# Generated by Django 4.0.9 on 2023-02-25 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_service_change_date_service_entity_service_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.servicename', verbose_name='Наименование'),
        ),
    ]
