from stock.models import Ingresos
from django.urls import path
from stock import views

urlpatterns = [
    path('',views.index, name='index'),
    path('altaprod/',views.cargar_producto, name="altaprod"),
    path('product/list', views.ListProductos.as_view(), name= 'productlist'),
    path('ingreso/', views.IngresoProducto.as_view(), name= 'ingreso')
]
