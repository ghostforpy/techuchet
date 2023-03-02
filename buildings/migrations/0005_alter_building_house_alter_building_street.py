# Generated by Django 4.0.9 on 2023-03-02 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0004_alter_building_options_alter_buildingtype_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='house',
            field=models.CharField(max_length=8, verbose_name='Дом'),
        ),
        migrations.AlterField(
            model_name='building',
            name='street',
            field=models.CharField(max_length=25, verbose_name='Улица'),
        ),
    ]
