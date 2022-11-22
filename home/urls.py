"""base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.home, name='home'),
    path("<int:pk>/", views.recipeDetail, name='recipe-detail'),
    path("<int:pk>/update-recipe/", views.updateRecipe, name='update-recipe'),
    path("<int:pk>/delete-recipe/", views.deleteRecipe, name='delete-recipe'),
    path("add-recipe/", views.addRecipe, name='add-recipe'),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),
    
    path("administrator/", views.administrator, name='administrator'),
    path("administrator/<int:pk>/update-user/", views.updateUser, name='update-user'),
    path("administrator/<int:pk>/delete-user/", views.deleteUser, name='delete-user'),
    path("administrator/view-contacts/", views.viewContacts, name='view-contacts'),
]