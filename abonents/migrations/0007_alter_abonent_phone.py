# Generated by Django 4.0.9 on 2023-02-26 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abonents', '0006_alter_objectstatus_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abonent',
            name='phone',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='Номер телефона'),
        ),
    ]