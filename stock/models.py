from django.db import models
from datetime import datetime
from django.forms import model_to_dict

from django.db.models.deletion import CASCADE

# Create your models here.
class product_group(models.Model):
    codigo= models.CharField(max_length=3, verbose_name= 'Codigo', unique=True)
    descripcion= models.CharField(max_length=30, verbose_name='Descripcion')

    def __str__(self):
        return self.descripcion
    class Meta:
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'
        ordering = ['id']
        db_table = 'Grupos'

class tipo(models.Model):
    codigo= models.CharField(max_length=3, verbose_name= 'Codigo', unique=True)
    descripcion= models.CharField(max_length=30, verbose_name='Descripcion')

    def __str__(self):
        return self.descripcion
    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['id']
        db_table = 'Tipos'

class cco(models.Model):
    codigo = models.CharField(max_length=10, verbose_name= "Codigo",unique=True)
    descripcion= models.CharField(max_length=30,verbose_name= "Descripcion")

    def __str__(self):
        return self.descripcion
    class Meta:
        verbose_name = 'Centro de Costo'
        verbose_name_plural = 'Centro de Costos'
        ordering = ['id']
        db_table = 'CCO'

class Producto(models.Model):
   grupo= models.ForeignKey(product_group, on_delete=models.CASCADE)
   tipo= models.ForeignKey(tipo, on_delete=CASCADE)
   codigo = models.CharField(max_length=50, verbose_name='Codigo', null= True, blank=True)
   descripcion = models.CharField(max_length=50, verbose_name='Descripcion')
   stock_minimo = models.PositiveIntegerField(default=0,verbose_name='Stock Minimo')
   stock = models.PositiveIntegerField(default=0, verbose_name='Stock Actual')
   cco = models.ForeignKey(cco, on_delete=CASCADE)
   date_created = models.DateField(auto_now=True)
   date_update = models.DateField(auto_now_add=True)
   
   
   def __str__(self):
       return self.descripcion

   class Meta:
       verbose_name = 'Producto'
       verbose_name_plural = 'Productos'
       ordering = ['id']
       db_table = 'Productos'

class retiro(models.Model):
    descripcion = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0, verbose_name='Cantidad')
    date = models.DateField(verbose_name="Fecha Retiro")
    ot = models.PositiveIntegerField(default=0,verbose_name="OT",null=True,blank=True)
    observacion = models.CharField(max_length=100, verbose_name="Observaciones")    

    def __str__(self):
       return self.cod_elemento

    class Meta:
       verbose_name = 'Retiro'
       verbose_name_plural = 'Retiros'
       ordering = ['id']
       db_table = 'Retiros'

class panol(models.Model):
    codigo = models.CharField(max_length=10,verbose_name='Codigo', unique=True)
    descripcion = models.CharField(max_length=20,verbose_name='Descripcion')
    
    def __str__(self):
       return self.descripcion

    class Meta:
       verbose_name = 'Pañol'
       verbose_name_plural = 'Pañoles'
       ordering = ['id']
       db_table = 'Pañol'




class traspasos(models.Model):
    descripcion = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0, verbose_name='Cantidad')
    date = models.DateField(verbose_name="Fecha Traspaso")
    nro_panol = models.ForeignKey(panol, on_delete=models.CASCADE)
    observacion = models.CharField(max_length=100, verbose_name="Observaciones")    

    def __str__(self):
       return self.cod_elemento

    class Meta:
       verbose_name = 'Traspasos'
       verbose_name_plural = 'Traspasos'
       ordering = ['id']
       db_table = 'Traspasos'


class prestamos(models.Model):
    descripcion = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0, verbose_name='Cantidad')
    fecha_retiro = models.DateField(verbose_name="Fecha Retiro")
    fecha_Devolucion = models.DateField(verbose_name="Fecha Retiro")
    observacion = models.CharField(max_length=100, verbose_name="Observaciones")    

    def __str__(self):
       return self.cod_elemento

    class Meta:
       verbose_name = 'Prestamo'
       verbose_name_plural = 'Prestamos'
       ordering = ['id']
       db_table = 'Prestamos'


class Ingresos(models.Model):
    descripcion = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0, verbose_name='Cantidad')
    date = models.DateField(verbose_name="Fecha Ingreso")
    nro_remito = models.PositiveIntegerField(default=0,verbose_name="Remito",null=True,blank=True)
    nro_rq = models.PositiveIntegerField(default=0,verbose_name="Requerimiento",null=True,blank=True)
    observacion = models.CharField(max_length=100, verbose_name="Observaciones")    

    def __str__(self):
       return self.cod_elemento

    def toJSON(self):
        item = model_to_dict(self)
        item['descripcion'] = self.descripcion.toJSON()
        item['cantidad'] = format(self.cantidad, '.2f')
        item['nro_remito'] = format(self.nro_remito, '.2f')
        item['cantnro_rqidad'] = format(self.nro_rq, '.2f')
        item['observacion'] = self.observacion.toJSON()
        item['date'] = self.date_joined.strftime('%d-%m-%Y')
        return item

    class Meta:
       verbose_name = 'Ingreso'
       verbose_name_plural = 'Ingresos'
       ordering = ['id']
       db_table = 'Ingresos'      

