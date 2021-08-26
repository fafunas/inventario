from stock.models import Producto, product_group, tipo
from django.contrib import admin

# Clases 

class ProductoAdmin (admin.ModelAdmin):
    fields=['grupo','tipo','descripcion','stock_minimo']
    list_display=['grupo','tipo','descripcion','stock_minimo','date_created','date_update']

class Gropuadmin (admin.ModelAdmin):
    fields=['codigo','descripcion']
    list_display=['codigo','descripcion']

class Tipoadmin (admin.ModelAdmin):
    fields=['codigo','descripcion']
    list_display=['codigo','descripcion']

#Registro de modelos
admin.site.register(product_group, Gropuadmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(tipo,Tipoadmin)

