from app2.views import *
from django.urls import path

app_name='employee'
urlpatterns=[
    path('lokesh/',lokesh,name='lokesh'),
]