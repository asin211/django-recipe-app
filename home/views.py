from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, Group
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from .decorators import *
from users.models import User
from users.forms import *


def home(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'home/home.html', context)


def recipeDetail(request, pk):
    recipe = Recipe.objects.get(id=pk)
    ingredients = recipe.ingredients.split(",")
    reviews = Recipe.objects.get(id=pk).review_set.all()
    if request.user.is_anonymous:
        if request.method == 'POST':
            messages.info(request, 'Please Login to review our Recipe')
    else:
        if request.method == 'POST':
            review = request.POST.get('review')
            recipe_id = Recipe.objects.get(id=pk)
            comment_by = User.objects.get(id=request.user.id)
            addReview = Review(comment_by=comment_by, recipe_id=recipe_id, review=review)
            addReview.save()
       
    context = {'recipe': recipe, 'ingredients': ingredients, 'reviews': reviews}
    return render(request, 'home/recipe-detail.html', context)


@login_required(login_url='login')
@manager_and_admin_only
# @allowed_users(allowed_roles=['Admins', 'Managers'])
def updateRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    form = AddRecipe(instance=recipe)

    if request.method == 'POST':
        form = AddRecipe(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'home/add-recipe.html', context)


@login_required(login_url='login')
@manager_and_admin_only
# @allowed_users(allowed_roles=['Admins', 'Managers'])
def deleteRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)

    if request.method =='POST':
        recipe.delete()
        return redirect('home')
    context ={'obj': recipe}
    return render(request, 'home/delete.html', context)


@login_required(login_url='login')
@manager_and_admin_only
# @allowed_users(allowed_roles=['Admins', 'Managers'])
def addRecipe(request):
    # if request.method == 'POST' and request.FILES['filename']:
    #     name = request.POST.get('name')
    #     ingredients = request.POST.get('ingredients')
    #     method = request.POST.get('method')
    #     image = request.FILES.get("filename") 
    #     created_by = User.objects.get(id=request.user.id)
    #     add_Recipe = Recipe(name=name, ingredients=ingredients, method=method, thumbnail=image, created_by=created_by)
    #     add_Recipe.save()
    #     messages.success(request, ' Your Recipe has been created!')
    #     return redirect('home')
    
    form = AddRecipe
    if request.method == 'POST':
        # print(request.POST)
        form = AddRecipe(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'home/add-recipe.html', context)


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        message = Contact(name=name, email=email, phone=phone,
                          desc=desc, date_created=datetime.today())
        message.save()
        messages.success(request, ' Your message has been sent!')
        return redirect('home')
    return render(request, 'home/contact.html')


@login_required(login_url='login')
@admin_only
# @allowed_users(allowed_roles=['Admins',])
def administrator(request):
    adminUsers = User.objects.filter(role="Admin")
    managers = User.objects.filter(role="Manager")
    normalUsers = User.objects.filter(role="User")
    context = {'adminUsers': adminUsers, 'managers': managers, 'normalUsers': normalUsers}
    return render(request, 'home/administrator.html', context)


@login_required(login_url='login')
@admin_only
# @allowed_users(allowed_roles=['Admins',])
def viewContacts(request):
    contacts = Contact.objects.all()
    context= {'contacts': contacts}
    return render(request, 'home/view-contacts.html', context)



@login_required(login_url='login')
@admin_only
# @allowed_users(allowed_roles=['Admins',])
def deleteUser(request, pk):
    user = User.objects.get(id=pk)
    if request.method =='POST':
        user.delete()
        return redirect('administrator')
    context ={'obj': user}
    return render(request, 'home/delete.html', context)


@login_required(login_url='login')
@admin_only
# @allowed_users(allowed_roles=['Admins',])
def updateUser(request, pk):
    user = User.objects.get(id=pk)
    form = CustomUserChangeForm(instance=user)

    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Details updated successfully for ' + user)
            return redirect('administrator')
    context = {'form': form}
    return render(request, 'home/update-user.html', context)




