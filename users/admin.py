from django.contrib import admin
from .models import * 

from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):

    list_display = ['name', 'email', 'username', 'role', 'is_staff', 'is_superuser', 'date_joined', ]

    fieldsets = UserAdmin.fieldsets = (
        (None, {
            "fields": (
                'name', 'email', 'username', 'role', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'date_joined', 'password',
            ),
        }),
    )

    # add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('name','email',)}),)
    add_fieldsets = ((None, {'fields': ('name','email',)}),) + UserAdmin.add_fieldsets

    

# Register your models here.
# admin.site.register(User)
admin.site.register(User, CustomUserAdmin)

