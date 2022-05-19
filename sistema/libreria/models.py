from ast import Delete
from contextlib import nullcontext
from distutils.command.upload import upload
from django.db import models
from django.forms import CharField

class libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    imagen = models.ImageField(null = True, verbose_name='Imagen')
    descripcion = models.TextField(null=True, verbose_name='Descripción')


    def __str__(self):
        fila = "Titulo: " + self.titulo
        return fila

    def Delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()