from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class cliente(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    vehiculo = models.CharField(max_length=20)
    desperfecto = models.CharField(max_length=20, null = True)

    def __str__(self) -> str:
        return f' {self.nombre} {self.apellido} - {self.vehiculo} - {self.desperfecto}'

    

class mecanico(models.Model):
    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50, null = True)


    def __str__(self) -> str:
        return f' {self.nombre} {self.apellido} - {self.especialidad} '


class Reparacion(models.Model):
    desperfecto = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=140, null=True)
    imagen = models.ImageField(upload_to='imagenes', blank=True, null = True)
    fechaDeEntrega = models.DateField()
    video = models.URLField( max_length=200, null = True)

    
   
    def __str__(self) -> str:
        return f' {self.desperfecto} - {self.fechaDeEntrega}'



class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', blank=True, null= True)