# Generated by Django 4.0.9 on 2023-02-26 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abonents', '0005_abonent_change_date_abonent_contract_abonent_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectstatus',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Наименование'),
        ),
    ]