from django.shortcuts import render, redirect
from .form import EmployeeForm
from .models import Employee
from django.views import View
# Create your views here.


def form(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view')
    else:
        form = EmployeeForm()

    show = {'form': form}
    return render(request, 'forms.html',show)



def view(request):
    if request.method == 'GET':
        Employees = Employee.objects.all()
        
    show = {'Employees': Employees}
    return render(request,'view.html',show)

def delete(request, id):
    form = Employee.objects.get(id=id)
    if request.method == 'POST':
        form.delete()
        return redirect('/')
    return render(request, 'delete.html')


def edit(request, id):
    data = Employee.objects.get( id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('view')
    else:
        form = EmployeeForm(instance=data)
    
    return render(request, 'edit.html', {'form': form, 'data': data})