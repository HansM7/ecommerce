from django.shortcuts import render
from store.models import Product
# Create your views here.

def home(request):
    data=Product.objects.all().filter(is_available=True)
    return render(request,'home.html',{'data':data})