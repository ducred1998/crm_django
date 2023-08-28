from django.contrib import admin
from .models import *

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer','product','date_created','status',)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'date_created',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'date_created',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Tag)