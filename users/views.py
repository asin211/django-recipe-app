from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from .models import *
from .forms import *
from .decorators import *


# Create your views here.

@unauthenticated_user
def registerUser(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():  
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='Users')
            user.groups.add(group)

            messages.success(request, 'Account created successfully for ' + username)
            return redirect('login')
        # else:
            # messages.error(request, 'An error occurred during registration. Please make sure password is 8 character long')  
        else:
            messages.info(
            request, form.errors)
    context = {'form': form}
    return render(request, 'users/registration/register.html', context)


@unauthenticated_user
def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # check if user credentials are right
        user = authenticate(username=username, password=password)
        # user = authenticate(request, username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")
            # return redirect("home")
        else:
            # No backend authenticated the credentials
            messages.info(
                request, 'Username or Password is incorrect!')   
    return render(request, 'users/registration/login.html')


def logoutUser(request):
    logout(request)
    return redirect('home')



