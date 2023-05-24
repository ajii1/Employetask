from django.contrib import admin
from .models import Employee
# Register your models here.

@admin.register(Employee)
class DataAdmin(admin.ModelAdmin):
    list_display = ['name',
        
        'email',
        'phone',
        'designation', 
        'address', 
        
        ]