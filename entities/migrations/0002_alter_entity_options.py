# Generated by Django 4.0.9 on 2023-02-26 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entity',
            options={'ordering': ['id'], 'verbose_name': 'Сущность', 'verbose_name_plural': 'Сущности'},
        ),
    ]
