from django.urls import path
from . import views


#Tempate Taggin
app_name = 'basic_app'

urlpatterns = [
    path('relative', views.relative, name = 'relative'),
    path('other', views.other, name = 'other'),
    # path('base',views.base, name = 'base')
]
