from stock.models import Producto, product_group, tipo
from django.contrib import admin

# Register your models here.

class ProductoAdmin (admin.ModelAdmin):
    fields=['grupo','tipo','descripcion']
    list_display=['grupo','tipo','descripcion','date_created','date_update']

class Gropuadmin (admin.ModelAdmin):
    fields=['Codigo','Descripcion']
   # list_display=['Codigo','Descripcion']

class Tipoadmin (admin.ModelAdmin):
    fields=['codigo','Descripcion']
    list_display=['codigo','Descripcion']

admin.site.register(product_group, Gropuadmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(tipo)