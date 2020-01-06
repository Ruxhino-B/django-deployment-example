from django.shortcuts import render
from apptwo.models import Users
# Create your views here.
def users(request):
    users_list = Users.objects.order_by('first_name')
    name_dict = {'name_records':users_list}
    return render(request,'index/users.html', context = name_dict)
