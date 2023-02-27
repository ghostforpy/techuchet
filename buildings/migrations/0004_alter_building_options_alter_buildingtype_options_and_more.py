# Generated by Django 4.0.9 on 2023-02-26 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0003_alter_regiontype_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='building',
            options={'ordering': ['id'], 'verbose_name': 'Здание', 'verbose_name_plural': 'Здания'},
        ),
        migrations.AlterModelOptions(
            name='buildingtype',
            options={'ordering': ['id'], 'verbose_name': 'Тип здания', 'verbose_name_plural': 'Типы зданий'},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'ordering': ['id'], 'verbose_name': 'Регион', 'verbose_name_plural': 'Регионы'},
        ),
        migrations.AlterModelOptions(
            name='regiontype',
            options={'ordering': ['id'], 'verbose_name': 'Тип региона', 'verbose_name_plural': 'Типы регионов'},
        ),
    ]