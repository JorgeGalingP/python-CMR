from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('account_home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups
                
                for role in allowed_roles:
                    if group.filter(name=role).exists():
                        return view_func(request, *args, **kwargs) 

            return HttpResponse('You are not authorized to view this page!')  
        return wrapper_func
    return decorator


def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()
            group_names = request.user.groups.values_list('name', flat=True)
            
            if 'customer' in group_names:
                return redirect('account_user')

            if 'admin' in group_names:
                return view_func(request, *args, **kwargs) 

        return HttpResponse('You are not authorized to view this page!')  
    return wrapper_func
