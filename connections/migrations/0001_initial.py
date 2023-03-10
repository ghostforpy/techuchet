# Generated by Django 4.0.9 on 2023-02-15 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('abonents', '0002_objectstatus_abonent_object_status'),
        ('services', '0002_service_abonent'),
        ('nodes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConnectionUnitType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Тип интерфейса',
                'verbose_name_plural': 'Типы интерфейсов',
            },
        ),
        migrations.CreateModel(
            name='ConnectionUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nodes.node', verbose_name='Логическое устройство')),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='services.service', verbose_name='Сервис')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='abonents.objectstatus', verbose_name='Статус')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='connections.connectionunittype', verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Интерфейс',
                'verbose_name_plural': 'Интерфейсы',
            },
        ),
    ]
