# Generated by Django 4.0.9 on 2023-02-16 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodes', '0003_alter_node_entity_delete_entity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='change_date',
            field=models.DateField(auto_now=True, verbose_name='Дата изменения'),
        ),
        migrations.AlterField(
            model_name='node',
            name='created_date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата создания'),
        ),
    ]
