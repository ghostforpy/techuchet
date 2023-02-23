# Generated by Django 4.0.9 on 2023-02-23 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0001_initial'),
        ('connections', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='connectionunit',
            name='entity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='entities.entity', verbose_name='Сущность'),
        ),
        migrations.AddField(
            model_name='connectionunit',
            name='number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Порядковый номер интерфейса'),
        ),
        migrations.AddField(
            model_name='connectionunit',
            name='rate',
            field=models.FloatField(blank=True, null=True, verbose_name='Пропускная способность'),
        ),
    ]
