# Generated by Django 5.1.2 on 2024-11-05 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_encuesta_pregunta_respuesta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pregunta',
            name='encuesta',
        ),
        migrations.RemoveField(
            model_name='respuesta',
            name='pregunta',
        ),
        migrations.RemoveField(
            model_name='respuesta',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Encuesta',
        ),
        migrations.DeleteModel(
            name='Pregunta',
        ),
        migrations.DeleteModel(
            name='Respuesta',
        ),
    ]
