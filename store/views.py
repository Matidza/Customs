from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms


# home page Route/View
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})


# About bage
def about(request):
    return render(request, 'about.html', {})


# Login
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, ('Login Was Successful!'))
            return redirect('home')

        else:
            messages.success(request, ('Login Not Successful! Try Again!!'))
            return redirect('login')
        
    else:
        return render(request, 'login.html', {})


# Logout
def logout_user(request):
    logout(request)
    messages.success(request, ("Logged Out!"))
    return redirect('home')


# Register Users
def register_user(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('Registration Forms Submitted Successfully. '))
            return redirect('home')
        
        else:
            messages.success(request, ('Registration Not Successfully. Try Again!!'))
            return redirect('register')   
    else:
        return render(request, 'register.html', {'form':form})
    
    
"""
def register_user(request):
	form = SignUpForm()
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			# log in user
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ("Username Created - Please Fill Out Your User Info Below..."))
			return redirect('home')
		else:
			messages.success(request, ("Whoops! There was a problem Registering, please try again..."))
			return redirect('register')
	else:
		return render(request, 'register.html', {'form':form})"""


# Individual product page
def product(request, pk):

    # Query the DB table to get product id for each selected product
    product = Product.objects.get(id=pk)

    # pass the product to the product.html file to be viewed/shown
    return render(request, 'product.html', {'product':product} )


# Category page later will be used as a search filter
def category(request, cat):
    cat=cat.replace('-', ' ')
    # filter the Category Model by product category
    
    try:
        category = Category.objects.get(name=cat)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products':products, 'category':category})
        #return render(request, 'category.html', {'product':product, 'category':category})


    except:
        messages.success(request, ("Category Doesn't Exist!"))
        return redirect('home')

#test
def all(request):
    all = Category.objects.all()

    return render(request, 'all.html', {'all': all})