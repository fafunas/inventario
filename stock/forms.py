from django.db.models.base import Model
from django.forms import ModelForm
from .models import Producto


class CargarForm(ModelForm):

    class Meta:
        model = Producto
        fields = ['grupo','tipo','descripcion','stock_minimo']
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
