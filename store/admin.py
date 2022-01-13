from django.contrib import admin
from .models import Product
# Register your models here.

class Productadmin(admin.ModelAdmin):
    list_display = ('product_name','product_price','product_description','product_stock','category','updated_date','is_available')

    prepopulated_fields={'product_slug':['product_name']}

admin.site.register(Product,Productadmin)