from django.urls import path
from . import views

urlpatterns = [
    path('', views.form, name='form'),
    path('view/', views.view, name='view'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('edit/<int:id>/', views.edit , name='edit')
    
]