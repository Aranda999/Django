# Generated by Django 5.1.2 on 2024-11-05 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_pregunta_encuesta_remove_respuesta_pregunta_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('imagen', models.ImageField(upload_to='imagenes/')),
            ],
        ),
    ]
