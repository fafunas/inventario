import json
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import RequestContext, context, loader
from django.views.generic.edit import FormView
from stock.forms import *
from stock.models import *
from django.views.generic import ListView, CreateView
from django.forms import formset_factory
from django.urls import reverse_lazy
from django.http import JsonResponse


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
            cco= form.cleaned_data['cco']

            newdoc = Producto(grupo = grupo, tipo = tipo, descripcion = descripcion, stock_minimo = stock_minimo, cco=cco)
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
class IngresoProducto(CreateView):
    model = Ingresos
    form_class = IngresoProd
    template_name = 'stock/ingreso.html'
    success_url = reverse_lazy('index')
    url_redirect = success_url

      
    def post(self, request, *args, **kwargs):
        if request.is_ajax:
            palabra = request.POST['term']
            print(palabra)
            libro = Producto.objects.filter(descripcion__icontains=palabra)
            results = []
            for i in libro:
                item = i.toJSON()
                item['value'] = i.name
                results.append(item)
        else:
            data_json = "fallo"
        mimetype = "application/json"
        return HttpResponse(data_json, mimetype)
        
