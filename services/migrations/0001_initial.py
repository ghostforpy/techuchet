# Generated by Django 4.0.9 on 2023-02-15 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Тип сервиса',
                'verbose_name_plural': 'Типы сервисов',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_created=True, verbose_name='Дата создания')),
                ('name', models.CharField(max_length=25, unique=True, verbose_name='Наименование')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.servicetype', verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Сервис',
                'verbose_name_plural': 'Сервисы',
            },
        ),
    ]
