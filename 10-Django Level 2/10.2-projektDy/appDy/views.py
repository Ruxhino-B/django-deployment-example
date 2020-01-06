from django.shortcuts import render
from appDy.models import Topic,Webpage,AccessRecord1

# Create your views here.
def index(request):
    my_dict = {'insert_content':'Hej ckemi'}
    return render(request, 'index/index.html', context = my_dict)
