# Generated by Django 4.0.9 on 2023-02-25 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nodes', '0009_alter_node_parent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='node',
            old_name='buiilding',
            new_name='building',
        ),
    ]
