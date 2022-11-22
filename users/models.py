from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    # pass
    ROLE = (
        ('Admin', 'Admin'),
        ('Manager', 'Manager'),
        ('User', 'User'),
    )
    role = models.CharField(max_length=30, choices=ROLE, default="User")

    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
            
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_joined', ]
