from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import RequestContext, loader
from stock.forms import CargarForm
from stock.models import Producto, product_group, tipo

# Create your views here.

def index(request):

    return render (request, 'stock/index.html')

   
def cargar_producto(request):
    if request.method == 'POST':
        form = CargarForm(request.Post)

        if form.is_valid():
            grupo = form.cleaned_data['grupo']
            tipo = form.cleaned_data['tipo']
            descripcion = form.cleaned_data['descripcion']
            stock_minimo = form.cleaned_data['stock_minimo']

            newdoc = Producto(grupo=grupo, tipo= tipo, descripcion= descripcion, stock_minimo= stock_minimo)
            newdoc.save()
            return redirect("index")
    else:
        form =CargarForm()
    return render(request, 'stock/alta_prod.html', {'form':form})
    
    