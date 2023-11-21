from app1.views import *
from django.urls import path

app_name='friendship'
urlpatterns=[
    path('kumar/',kumar,name='kumar')
]