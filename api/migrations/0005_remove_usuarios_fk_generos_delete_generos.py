# Generated by Django 5.1.2 on 2024-10-30 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_usuarios_fk_generos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='fk_generos',
        ),
        migrations.DeleteModel(
            name='Generos',
        ),
    ]
