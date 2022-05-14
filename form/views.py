from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def home(request):
    return render(request, 'form/index.html')

def project(request):
    users = customer.objects.all()
    form = CustomerForm()
    if request.method == 'POST':
        print(request.POST)
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/project')
    

    username = request.GET.get('Name')
    users = users.filter(name = username)
    context = {'form': form, "users": users}
    return render(request, 'form/project.html', context)
