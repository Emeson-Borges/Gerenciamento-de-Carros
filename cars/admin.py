from django.contrib import admin
from .models import Car

# Register your models here.

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'value')
    list_filter = ('model', 'brand', 'factory_year', 'value')
    search_fields = ('model', 'brand', 'factory_year', 'value')


admin.site.register(Car, CarAdmin)