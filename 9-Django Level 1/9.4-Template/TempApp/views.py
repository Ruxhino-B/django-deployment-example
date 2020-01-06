from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    dictionary = {'kodi_im':"Un jam serisht dicka e importuar nga template/new-template"}
    return render(request,'new_templates/index.html', context = dictionary)
