from django.shortcuts import redirect


def login_required():
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator


def check_user_role(required_role):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user == "AnonymousUser" or not hasattr(request.user, 'rol') or request.user.rol != required_role:
                return redirect('administracion_login')
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator