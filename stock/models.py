from django.db import models
from datetime import datetime

from django.db.models.deletion import CASCADE

# Create your models here.
class product_group(models.Model):
    codigo= models.CharField(max_length=3, verbose_name= 'Codigo')
    descripcion= models.CharField(max_length=30, verbose_name='Descripcion')

    def __str__(self):
        return self.descripcion
    class Meta:
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'
        ordering = ['id']
        db_table = 'Grupos'

class tipo(models.Model):
    codigo= models.CharField(max_length=3, verbose_name= 'Codigo')
    descripcion= models.CharField(max_length=30, verbose_name='Descripcion')

    def __str__(self):
        return self.descripcion
    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['id']
        db_table = 'Tipos'

class Producto(models.Model):
   grupo= models.ForeignKey(product_group, on_delete=models.CASCADE)
   tipo= models.ForeignKey(tipo, on_delete=CASCADE)
   codigo = models.CharField(max_length=50, verbose_name='Codigo', null= True, blank=True)
   descripcion = models.CharField(max_length=50, verbose_name='Descripcion')
   date_created = models.DateField(auto_now=True)
   date_update = models.DateField(auto_now_add=True)
   stock_minimo = models.PositiveIntegerField(default=0,verbose_name='Stock Minimo')
   

   def __str__(self):
       return self.descripcion

   class Meta:
       verbose_name = 'Producto'
       verbose_name_plural = 'Productos'
       ordering = ['id']
       db_table = 'Productos'

    





