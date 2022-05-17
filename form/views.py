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
    check = bool(username)
    for i in list(users):
        if username == i.name or username == '':
            check = False
    filteredUsers = users.filter(name = username)
    if username == "_all_" or username == "_All_":
        filteredUsers = users
        check = False
    context = {'form': form, "users": filteredUsers, "check":check}
    return render(request, 'form/project.html', context)
