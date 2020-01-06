from django.shortcuts import render
# from django.http import HttpResponse
# from basicapp2.models import Users
from basicapp2.forms import NewUsers
# Create your views here.
def index(request):
    return render(request,'index/basicapp2.html')

def basicapp2(request):
    form = NewUsers()
    if request.method == "POST":
        form = NewUsers(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error Form Invalid')
    return render(request,'index/basicapp2.html',{'form':form})
