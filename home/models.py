from django.db import models
from users.models import User

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    method = models.TextField()
    thumbnail = models.ImageField(null=False, blank=False)
    date_created = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
    # updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_created', 'name']


class Review(models.Model):
    comment_by = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    review = models.CharField(max_length=100, null=False, blank=False)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.review

    class Meta:
        ordering = ['-date_created', 'review']


class Contact(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False)
    email = models.EmailField(max_length=30, null=False, blank=False)
    phone = models.CharField(max_length=15, null=True, blank=True)
    desc = models.TextField(null=False, blank=False)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_created', '-name']


