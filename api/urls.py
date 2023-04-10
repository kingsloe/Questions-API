from django.urls import path
from .views import *

urlpatterns = [
    path('questions/', questions_list, name='questions_list')
]
