from django.http import HttpResponse
from django.shortcuts import redirect


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            # print('Testing.. ', allowed_roles)
            # return view_func(request, *args, **kwargs)
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('<h2>You are not authorized to view this page</h2>')
        return wrapper_func
    return decorator


# # permissions targeting groups
# def admin_only(view_func):
#     def wrapper_func(request, *args, **kwargs):
#         # print('Testing.. ', allowed_roles)
#         # return view_func(request, *args, **kwargs)
#         group = None
#         if request.user.groups.exists():
#             group = request.user.groups.all[0].name
        
#         if group == 'Users':
#             # return redirect ('home')
#             return HttpResponse('You are not authorized to view this page')

#         if group == 'Admins':
#             return view_func(request, *args, **kwargs)
    
#     return wrapper_func

# # permissions targeting groups
# def manager_and_admin_only(view_func):
#     def wrapper_func(request, *args, **kwargs):
#         # print('Testing.. ', allowed_roles)
#         # return view_func(request, *args, **kwargs)
#         group = None
#         if request.user.groups.exists():
#             group = request.user.groups.all[0].name
        
#         if group == 'Users':
#             # return redirect ('home')
#             return HttpResponse('You are not authorized to view this page')

#         if group == 'Admins' or group == 'Managers':
#             return view_func(request, *args, **kwargs)
    
#     return wrapper_func


# permissions targeting role
def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        # print('Testing.. ', allowed_roles)
        # return view_func(request, *args, **kwargs)
        role = request.user.role

        if role == 'Admin':
            return view_func(request, *args, **kwargs)
        else:
            # return redirect ('home')
            return HttpResponse('<h2>You are not authorized to view this page</h2>')
    
    return wrapper_func

# permissions targeting role
def manager_and_admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        role = request.user.role

        if role == 'Admin' or role == 'Manager':
            return view_func(request, *args, **kwargs)
        else:
            # return redirect ('home')
            return HttpResponse('<h2>You are not authorized to view this page</h2')
    
    return wrapper_func
