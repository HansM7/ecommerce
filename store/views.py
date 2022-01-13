from django.shortcuts import get_object_or_404, render
from .models import Product
from category.models import Category
# Create your views here.

def store(request,slug_category=None):

    categories=None
    products=None

    if slug_category !=None:
        categories=get_object_or_404(Category,category_slug=slug_category)
        products=Product.objects.filter(category=categories,is_available=True)
        product_count=products.count()
    else:
        products=Product.objects.filter(is_available=True)
        product_count=products.count()

    data_category=Category.objects.all()
    # data_product=Product.objects.all()
    # count_product=data_product.count()

    context = {
        'data_category':data_category,
        'data_product':products,
        'cantidad':product_count
    }

    return render(request,'store.html',context)

def details(request,id):
    data=Product.objects.get(id=id)

    return render(request,'detail.html',{'data':data})