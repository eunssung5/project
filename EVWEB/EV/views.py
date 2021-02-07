from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import *
from django.http import JsonResponse
from django.shortcuts import render, redirect

import csv
# Create your views here.

class EVListView(ListView):
    model = EV

class EVCreateView(CreateView):
    model = EV
    fields = ['site_name','url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'


class EVDetailView(DetailView):
    model = EV

def index(request):
    if request.session.get('user_id') and request.session.get('user_name'):
        context = {'id' : request.session['user_id'],
                   'name': request.session['user_name']                   }
        return render(request, 'home.html', context)
    else :
        return render(request, 'login.html')

def logout(request):
    request.session['user_name'] = {}
    request.session['user_id'] = {}
    request.session.modified    = True
    return redirect('index')
def loginProc(request):
    print('request - loginProc')
    if request.method =='GET':
        return redirect('index')
    elif request.method =='POST':
        id = request.POST['id']
        pwd = request.POST['pwd']

        #select * from bbsuserregister where user_id = id and user_pwd = pwd
        # orm: class - table
        user = EVUserRegister.objects.get(user_id = id , user_pwd=pwd)
        print('user result - ', user)
        context = {}
        if user is not None:
            request.session['user_name'] = user.user_name
            request.session['user_id'] = user.user_id
            context['name']=request.session['user_name']
            context['id']=request.session['user_id']
            return render(request , 'home.html',context)
        else :
            return redirect('index')

def registerForm(request):
    print('request - registerForm')
    return render(request, 'join.html')

def register(request):
    #id,pwd,name -> model -> db(insert)
    if request.method == 'POST' :
        id = request.POST['id']
        pwd = request.POST['pwd']
        name = request.POST['name']
        register = EVUserRegister(user_id = id , user_pwd = pwd , user_name = name)
        register.save()
    return render(request, 'login.html')





def naverMapEx1(request):
    print("check - success load map")
    return render(request, 'naverMapApiEx1.html')

def naverMapEx2(request):
    print("check - success load map")
    return render(request, 'naverMapApiEx2.html')

def naverMapEx3(request):
    print("check - success load map")
    return render(request, 'naverMapApiEx3.html')






