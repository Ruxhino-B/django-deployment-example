from django.shortcuts import render

def index(request):
    kodi = {'kodi_im':"help page"}
    return render(request,'temp-app/index.html', context = kodi)
