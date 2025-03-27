from django.contrib import admin
from .models import Imagen
from django.utils.html import format_html


@admin.register(Imagen)
class ImagenAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descripcion', 'mostrar_imagen']
    search_fields = ['titulo', 'descripcion']
    list_filter = ['titulo']

    def mostrar_imagen(self, obj):
        # Devuelve una vista previa de la imagen en el panel de administración
        return format_html('<img src="{}" width="100" height="100" />', obj.imagen.url)
    mostrar_imagen.short_description = 'Imagen'