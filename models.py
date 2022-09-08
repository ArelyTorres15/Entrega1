from django.db import models

# Create your models here.

class Ropa(models.Model):
    descripcion=models.CharField(max_length=50)
    precio=models.IntegerField()

    def __str__(self):
        return self.descripcion+" "+str(self.precio)


class Clientes(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()

    def __str__(self):
        return self.nombre+" "+self.apellido
        

class Staff(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()
    profesion= models.CharField(max_length=50)

    def __str__(self):
        return self.nombre+" "+self.apellido

class Envios(models.Model):
    nombre= models.CharField(max_length=50)
    fecha_entrega= models.DateField()
    entregado= models.BooleanField()