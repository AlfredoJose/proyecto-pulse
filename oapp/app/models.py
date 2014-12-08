from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
# Create your models here.

class Categoria(models.Model):
    titulo = models.CharField(max_length = 140)

    def __unicode__(self):
        return self.titulo


class Enlace(models.Model):
    titulo = models.CharField(max_length = 140)
    enlace = models.URLField()
    votos = models.IntegerField(default = 0)
    categoria = models.ForeignKey(Categoria)
    usuario = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='media/', blank=True, null=True)

    def __unicode__(self):
        return "%s -  %s" % (self.titulo,self.enlace)

admin.site.register(Categoria)
admin.site.register(Enlace)

