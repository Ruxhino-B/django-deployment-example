from django.urls import path
from tempApp import help
urlpatterns = [
    path('',help.index, name = 'index')
]
