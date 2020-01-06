from django.urls import path
from basicapp2 import views

urlpatterns = [
    # path('', views.index, name = 'index'),
    path('', views.basicapp2, name = 'basicapp2')
]
