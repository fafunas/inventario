from django.urls import path
from stock import views

urlpatterns = [
    path('',views.index, name='index'),
]
