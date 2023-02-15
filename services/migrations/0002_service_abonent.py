# Generated by Django 4.0.9 on 2023-02-15 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('abonents', '0002_objectstatus_abonent_object_status'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='abonent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='abonents.abonent', verbose_name='Абонент'),
        ),
    ]
