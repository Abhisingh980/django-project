from django.shortcuts import render

from django.http import HttpResponse


data_list = [
    {'name': 'John', 'age': 23},
    {'name': 'Doe', 'age': 33},
    {'name': 'Jane', 'age': 43},
    {'name': 'Doe', 'age': 53},
    {'name': 'Doe', 'age': 63},
    {'name': 'Abhinesh Kumar','age':24}
]


def index(request):
    return render(request, 'index.html',{'data': data_list,'page': 'index'})

def home(request):
    context = {'page': 'home'}
    return render(request, 'home.html',context=context)

def contact(request):
    context = {'page': 'contact'}
    return render(request, 'contact.html',context=context)

# Create your views here.
