from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import RequestContext, context, loader
from stock.forms import *
from stock.models import *
from django.views.generic import ListView

# Create your views here.

def index(request):

    return render (request, 'stock/index.html')


#Funcion para agregar producto a la DB   
def cargar_producto(request):
    if request.POST:
        form = CargarForm(request.POST)

        if form.is_valid():
            grupo = form.cleaned_data['grupo']
            tipo = form.cleaned_data['tipo']
            descripcion = form.cleaned_data['descripcion']
            stock_minimo = form.cleaned_data['stock_minimo']

            newdoc = Producto(grupo = grupo, tipo = tipo, descripcion = descripcion, stock_minimo = stock_minimo)
            newdoc.save()
            return redirect("index")
    else:
        form =CargarForm()
    return render(request, 'stock/alta_prod.html', {'form':form})
    

#Listado de productos

class ListProductos(ListView):
    model = Producto
    template_name = 'stock/listview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Productos'


        return context


#Ingresando producto al almacen, sumando stock
