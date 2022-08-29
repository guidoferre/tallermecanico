from django.db import models
from ckeditor.fields import RichTextField
from blog.models import cliente
from datetime import datetime, date

class Post(models.Model):
    nombre = models.CharField(max_length = 50, null = True)
    email = models.EmailField( max_length=254, null = True)
    titulo = models.CharField( max_length=250, null = True)
    contenido = RichTextField( blank=True, null = True)
    fecha = models.DateField(auto_now_add= True, null = True)

    def __str__(self):
        return f'{self.titulo} - {self.nombre}'

