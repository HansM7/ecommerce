from django.db import models
from category.models import Category

# Create your models here.

class Product(models.Model):
    product_name=models.CharField(max_length=50)
    product_slug=models.CharField(max_length=50)
    product_description=models.TextField(blank=True)
    product_price=models.FloatField()
    product_image=models.ImageField(upload_to="Productos")
    product_stock=models.IntegerField()

    is_available=models.BooleanField(default=True)
    

    category = models.ForeignKey(Category,  on_delete=models.CASCADE)

    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name