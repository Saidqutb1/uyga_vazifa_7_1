from django.contrib import admin
from .models import Category, Goods
# Register your models here.
admin.site.register(Goods)
admin.site.register(Category)