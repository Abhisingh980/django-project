from django.shortcuts import render , redirect
from .models import Fooddata
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
#decorator for login required
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login/')
def foodreview(request):
    if request.method == 'POST':
        foodname = request.POST['quearytext']
        description = request.POST['discription']
        word=description.split()
        if len(word) > 20:
            description = ' '.join(word[:20])
        image = request.FILES['imagefile']
        data = Fooddata(foodname=foodname, description=description, image=image)

        data.save()
        return redirect('/foodreview/')

    data = Fooddata.objects.all()

    if request.GET.get('search'):
        data = Fooddata.objects.filter(foodname__icontains=request.GET.get('search'))


    return render(request, 'foodreview.html', {'fooddata':data})
@login_required(login_url='/login/')
def deletequerry(request, id):
    querry = Fooddata.objects.get(id=id)
    if querry:
        querry.delete()
    return redirect('/foodreview/')
@login_required(login_url='/login/')
def updatequerry(request, id):
    querry = Fooddata.objects.get(id=id)
    if request.method == 'POST':
        querry.foodname = request.POST['quearytext']
        querry.description = request.POST['discription']
        if 'imagefile' in request.FILES:
            querry.image = request.FILES['imagefile']
        querry.save()
        return redirect('/foodreview/')
    return render(request, 'update.html', {'querry':querry})


def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid UserName')
            return render(request, 'login.html')

        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid credentials')
            return render(request, 'login.html')
        else:
            login(request, user)
            return redirect('/foodreview/')
    return render(request, 'login.html')

@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return redirect('/login/')


def register(request):
    if request.method == 'POST':
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'register.html')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return render(request, 'register.html', )
        if len(password) < 8:
            messages.error(request, 'Password must be 8 characters long')
            return render(request, 'register.html',)


        user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email)
        user.set_password(password)
        user.save()
        messages.success(request, 'User created successfully')
        return redirect('/login/')
    return render(request, 'register.html')
