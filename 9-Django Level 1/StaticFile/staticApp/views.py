from django.shortcuts import render

def index(request):
    cels = {'celsi':'Fotoja shpresoj qe te dali'}
    return render(request,'temp/index.html', context = cels)

# Create your views here.
