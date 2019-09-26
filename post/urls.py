from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'), 
    path('home/',views.home, name= 'home'),
    path('create/',views.create, name= 'create'),
    path('<slug>/', views.show, name='show'),
    path('edit/<int:pk>/', views.edit, name='edit'),  
    path('delete/<int:pk>', views.delete, name='delete'), 
    path('export', views.export, name='export'),
   
   
]