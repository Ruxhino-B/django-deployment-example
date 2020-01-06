from django.shortcuts import render
from django.http import HttpResponse
from appone.models import AccessRecord, Topic, Webpage


# Create your views here.
def index(request):
    Fjalor = {'brenda':'un jam brenda fjalorit'}
    return render(request, 'index/index.html', context = Fjalor)
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {"access_records":webpages_list}
    return render(request,'index/index.html',date_dict)
