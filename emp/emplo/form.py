from django import forms
from .models import Employee

from django import forms
from .models import Employee
    
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
           
        'name':'Employee Name', 
        'email' :'Email',
        'phone' :'Phone',
        'designation' :'Designation', 
        'address' : 'Address', 
        
        }

        