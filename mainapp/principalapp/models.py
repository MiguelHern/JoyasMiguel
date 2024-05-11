from django.db import models

# Create your models here.

class Proveedores(models.Model):
    nombre = models.CharField(max_length=255)
    img = models.FileField(upload_to='image-svc')
    status = models.CharField(max_length=20)


class Marcas(models.Model):
    nombre = models.CharField(max_length=255)
    img = models.FileField(upload_to='image-svc')
    noVenta = models.IntegerField()
    status = models.CharField(max_length=20)
    proveedor = models.ForeignKey(Proveedores, on_delete=models.SET_NULL, null=True) #Tambien esta el Cascade


class Productos(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.FileField(upload_to='image-svc')
    status = models.CharField(max_length=20)
    CATEGORIA_CHOICES = [
        ('charms', 'charms'),
        ('aretes', 'aretes'),
        ('anillos', 'anillos'),
        ('brazaletes', 'brazaletes'),
        ('collares', 'collares'),
    ]
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default='categoria1')
    proveedor = models.ForeignKey(Proveedores, on_delete=models.SET_NULL, null=True)  # Tambien esta el Cascade
    marca = models.ForeignKey(Marcas, on_delete=models.SET_NULL, null=True)