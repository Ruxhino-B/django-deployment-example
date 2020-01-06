from django.urls import path
from staticApp import views
urlpatterns = [
    path('', views.index, name = 'index')
]
