from django.contrib import admin
from .models import category,Products
# Register your models here.
class category_Admin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}


admin.site.register(category,category_Admin)

class product_Admin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','updated']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['price','stock','available']
    list_per_page = 20

admin.site.register(Products,product_Admin)