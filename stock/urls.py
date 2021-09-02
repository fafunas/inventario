from django.urls import path
from stock import views

urlpatterns = [
    path('',views.index, name='index'),
    path('altaprod/',views.cargar_producto, name="altaprod"),
    path('product/list', views.ListProductos.as_view(), name= 'productlist')
]
