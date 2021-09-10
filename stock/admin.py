from stock.models import Ingresos, Producto, cco, panol, prestamos, product_group, retiro, tipo, traspasos
from django.contrib import admin

# Clases 

class ProductoAdmin (admin.ModelAdmin):
    fields=['grupo','tipo','descripcion','cco','stock_minimo']
    list_display=['grupo','tipo','descripcion','cco','stock','stock_minimo','date_created','date_update']

class Gropuadmin (admin.ModelAdmin):
    fields=['codigo','descripcion']
    list_display=['codigo','descripcion']

class Tipoadmin (admin.ModelAdmin):
    fields=['codigo','descripcion']
    list_display=['codigo','descripcion']

class Ccoadmin (admin.ModelAdmin):
    fields=['codigo','descripcion']
    list_display=['codigo','descripcion']  

class Panoladmin (admin.ModelAdmin):
    fields=['codigo','descripcion']
    list_display=['codigo','descripcion']      

#Registro de modelos
admin.site.register(product_group, Gropuadmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(tipo,Tipoadmin)
admin.site.register(cco, Ccoadmin)
admin.site.register(panol,Panoladmin)
admin.site.register(retiro)
admin.site.register(traspasos)
admin.site.register(prestamos)
admin.site.register(Ingresos)


