# Generated by Django 4.0.9 on 2023-02-25 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nodes', '0010_rename_buiilding_node_building'),
    ]

    operations = [
        migrations.CreateModel(
            name='NodeName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Имя оборудования',
                'verbose_name_plural': 'Имена оборудования',
            },
        ),
        migrations.AlterField(
            model_name='node',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nodes.nodename', verbose_name='Наименование'),
        ),
    ]
