from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .forms import WeekForm
from .models import Week, DayEntry

# Create your views here.

@login_required
@permission_required('weeks.add_week', raise_exception=True)
def week_create(request):
    # Fase 1: GET → selector de fecha
    if request.method == 'GET':
        form = WeekForm()
        return render(request, 'weeks/week_create.html', {
            'form': form,
            'show_table': False
        })

    # POST con datos
    form = WeekForm(request.POST)
    # Fase 1 válida: mostrar tabla
    if form.is_valid() and 'day_0' not in request.POST:
        start = form.cleaned_data['start_day']
        return render(request, 'weeks/week_create.html', {
            'form': form,
            'show_table': True,
            'start_day': start
        })

    # Fase 2: guardar Week y DayEntry
    if form.is_valid() and 'day_0' in request.POST:
        week = Week.objects.create(
            start_day=form.cleaned_data['start_day'],
            created_by=request.user
        )
        # Crear los 7 DayEntry con los valores enviados
        for i in range(7):
            qty = int(request.POST.get(f'day_{i}', 0))
            DayEntry.objects.create(
                week=week,
                weekday=i,
                estimated_pizzas=qty
            )
        return redirect('weeks:detail', pk=week.pk)

    # Si llegamos aquí, hay validación fallida
    return render(request, 'weeks/week_create.html', {
        'form': form,
        'show_table': False
    })

@login_required
def week_detail(request, pk):
    """
    Vista sencilla que muestra la semana y sus días.
    """
    week = get_object_or_404(Week, pk=pk)
    # days está ordenado de lunes a domingo por Meta.ordering
    return render(request, 'weeks/week_detail.html', {
        'week': week,
        'days': week.days.all()
    })