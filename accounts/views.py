# accounts/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    """
    Esta función:
    - Sólo se ejecuta si ya has iniciado sesión (por @login_required).
    - request.user es el usuario que acaba de loguearse.
    - request.user.is_staff es True si ese usuario es administrador.
    """
    if request.user.is_staff:
        # El usuario tiene permiso de edición
        return render(request, 'has_permission.html')
    else:
        # El usuario no tiene permiso de edición
        return render(request, 'no_permission.html')
