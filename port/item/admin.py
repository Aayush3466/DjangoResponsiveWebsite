from django.contrib import admin

# Register your models here.
from .models import Category, Item, Value

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Value)
