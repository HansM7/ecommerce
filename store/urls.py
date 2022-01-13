from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.store, name="store"),
    path("<int:id>/",views.details, name="detail"),
    path("<slug:slug_category>/",views.store, name="products_by_category"),
    
]
