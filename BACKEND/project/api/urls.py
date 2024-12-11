from django.urls import path
from app import views 
urlpatterns =[
    path ('list_Chairperson/' , views.getChairperson),
]