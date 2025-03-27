from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Usuarios(models.Model):
    usuarios_id = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=255)
    class Meta:
        db_table = "usuarios"



class Imagen(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='imagenes/', blank=True, null=True)

    def __str__(self):
        return self.titulo
