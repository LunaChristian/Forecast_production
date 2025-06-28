from django.urls import path
from . import views

app_name = 'weeks'

urlpatterns = [
    # URL para editar una semana (solo staff)
    path('editar/<int:week_id>/', views.edit_week, name='edit'),
    # URL para ver la semana en modo solo lectura
    path('ver/<int:week_id>/', views.view_week, name='view'),
]
