
# Create your views here.
# crud/views.py

from django.shortcuts import render
from django.http import HttpResponse

data = {
    'name': 'Ram',
    'age': 20,
    'city': 'Delhi'
}

def welcome(request):
    return HttpResponse("Welcome to the Basic CRUD App!")

def create(request):
    print('request came to here')
    if request.method == 'POST':
        key = request.POST['key']
        value = request.POST['value']
        data[key] = value
    return render(request, 'create.html')

def read(request):
    return render(request, 'read.html', {'data': data})

def update(request):
    if request.method == 'POST':
        key = request.POST['key']
        value = request.POST['value']
        if key in data:
            data[key] = value
    return render(request, 'update.html')

def delete(request):
    if request.method == 'POST':
        key = request.POST['key']
        if key in data:
            del data[key]
    return render(request, 'delete.html')
