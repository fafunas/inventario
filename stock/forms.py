from django.db.models.base import Model
from django.forms import *
from .models import Ingresos, Producto

#Ingreso nueva producto
class CargarForm(ModelForm):

    class Meta:
        model = Producto
        fields = ['grupo','tipo','descripcion','stock_minimo','cco']
        error_messages = {
            'grupo': {
                'required': ("Se debe agregar un grupo"),
            },
            'tipo': {
              'required': ("Se debe agregar un tipo"),
            },
           'descripcion': {
               'required': ("Se debe agregar una descripcion del producto"),
            },
           'stock_minimo': {
               'required': ("El stock minimo debe ser mayor a 0"),
            }
            
       }
    def __init__(self, *args, **kwargs):
      super(CargarForm, self).__init__(*args, **kwargs)


#Ingreso producto al Stock
class IngresoProd(ModelForm):
    def __init__(self, *args, **kwargs):
      super(IngresoProd, self).__init__(*args, **kwargs)
      for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = Ingresos
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
      super(IngresoProd, self).__init__(*args, **kwargs)
