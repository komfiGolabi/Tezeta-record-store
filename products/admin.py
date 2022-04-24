from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Product, Category

# Register your models here.

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
