from django.contrib import admin
from .models import Product, ProductImage, Test

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Test)
