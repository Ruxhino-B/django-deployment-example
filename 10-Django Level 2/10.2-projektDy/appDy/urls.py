from django.urls import path
from appDy import views

urlpatterns = [
    path('', views.index, name = 'index')
]
