from django.shortcuts import render
from basic_app.form import FormProfilUserInfo,FormUser
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request,'index/index.html')
def register(request):

    registered = False

    if request.method == 'POST':
        user_form = FormUser(data=request.POST)
        profile_form = FormProfilUserInfo(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit = False)
            profile.user = user

            if 'Foto' in request.FILES:
                profile.Foto = request.FILES['Foto']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = FormUser()
        profile_form = FormProfilUserInfo()
    return render(request,'index/regjistrohu.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse('You are loggen in, Nice')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account not active')
        else:
            print('Some one tired to log in and failed!')
            print('UserName: {} and Password: {}'.format(username,password))
            return HttpResponse('invalid Login details supplied')
    else:
        return render (request,'index/login.html',{})
