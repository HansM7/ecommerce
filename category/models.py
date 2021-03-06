from django.db import models

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=50,unique=True)
    category_description=models.CharField(max_length=255,blank=True)
    category_slug=models.CharField(max_length=100,unique=True)

    category_image=models.ImageField( upload_to='Category', blank=True)

    class Meta:

        verbose_name = 'category'
        verbose_name_plural = 'categories'


    def __str__(self):
        return self.category_name
