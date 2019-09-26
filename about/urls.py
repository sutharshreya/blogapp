from django.urls import path
from . import views
# load urls.
urlpatterns = [
  
    path('contact/', views.contact, name='contact')
  
]