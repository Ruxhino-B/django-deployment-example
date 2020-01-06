from django.urls import path
from mapApp import views

urlpatterns = [
    path('', views.index, name = 'index')
]
