from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm
from django import forms
from django.http import  HttpResponse
from django.utils.translation import  gettext as _


# home page Route/View
def home(request):
    output = _("TEST")
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


# update User Account
def update_user(request):
	if request.user.is_authenticated:
        # What/Which user is authenticated/
		current_user = User.objects.get(id=request.user.id)
        # create form
		user_form = UpdateUserForm(request.POST or None, instance=current_user)

        # Validate  the form and its content and login user
		if user_form.is_valid():
			user_form.save()

			login(request, current_user)
			messages.success(request, "User Has Been Updated!!")
			return redirect('home')
		return render(request, "update_user.html", {'user_form':user_form})
	else:
		messages.success(request, "You Must Be Logged In To Access That Page!!")
		return redirect('home')
     
# update User Account
def update_password(request):
    # Authenticate User
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == 'POST':
            form = ChangePasswordForm(current_user, request.POST)

            if form.is_valid():
                form.save()
                messages.success(request, "Password Updated!!")
                login(request, current_user)
                return redirect('update_user')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                    return redirect('update_password')
        else:
            form = ChangePasswordForm(current_user)
            return render(request, "update_password.html", {'form':form})#          
    else:
        messages.success(request, "You Must Be Logged In To Access That Page!!")
        return redirect('home')               
    
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
    cat = cat.replace('-', ' ')
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