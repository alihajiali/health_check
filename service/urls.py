from django.urls import path
from .views import *

app_name = "service"

urlpatterns = [
    path('add_service/', add_service, name="add_service"), 
    path('services/', services, name="services"), 
    path('edit_service/<str:id>/', edit_service, name="edit_service"),  
    path('change_status/<str:service_name>/', change_status, name="change_status"),  
]