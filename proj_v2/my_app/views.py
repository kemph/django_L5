from django.shortcuts import render
from my_app.forms import UserForm , UserInfoForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'my_app/index.html')
def other(request):
    return render(request,'my_app/other.html')
def register(request):
    is_registered = False
    user_form = UserForm()
    profile_form = UserInfoForm()

    if request.method =='POST':
        user_form = UserForm( data = request.POST)
        profile_form = UserInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user

            if 'pic' in request.FILES:
                profile.pic = request.FILES['pic']

            profile.save()
            is_registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        print('NOT POST')
        user_form = UserForm()
        profile_form = UserInfoForm()
    return render(request,'my_app/register.html',{'user_form':user_form,'profile_form':profile_form,'is_registered':is_registered})

def user_login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('username {} and password {}'.format(username,password));
        user= authenticate(username = username, password = password)
        if user:
            print('authenticated')
            if user.is_active:
                print('{} is active'.format(username))
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                print('User Not active')
                return HttpResponse('User is not active')
        else:
            print('User Not authenticated')
            print('{} tried to login with pwd {}'.format(username,password))
            return HttpResponse('Invalid login supplied:/')
    else:
        print('not post')
        return render(request,'my_app/logon.html',{})

@login_required
def user_logout(request):
    print('user logging out')
    logout(request)
    return HttpResponseRedirect(reverse('index'))
