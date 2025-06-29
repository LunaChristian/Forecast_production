# weeks/urls.py
from django.urls import path
from . import views
from .views import week_create, week_detail

app_name = 'weeks'

urlpatterns = [
    # 1) Crear semana: Fase 1 (selector) y Fase 2 (tabla)
    path('create/', week_create, name='create'),

    # 2) Detalle de semana (tras guardar)
    path('detail/<int:pk>/', week_detail, name='detail'),

    # 3) Editar semana (ya existente)
    path('editar/<int:week_id>/', views.edit_week, name='edit'),

    # 4) Ver semana en solo lectura
    path('ver/<int:week_id>/', views.view_week, name='view'),

    # (Puedes renombrar history y current cuando las implementes)
    # path('history/', views.week_history, name='history'),
    # path('current/', views.current_week, name='current'),
]
