# weeks/forms.py
from django import forms
from django.core.exceptions import ValidationError
from .models import Week

class WeekForm(forms.ModelForm):
    class Meta:
        model = Week
        fields = ['start_day']
        widgets = {
            'start_day': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'id': 'startDayPicker',
                    'autocomplete': 'off'
                }
            ),
        }

    def clean_start_day(self):
        start = self.cleaned_data['start_day']
        # 1) Validar lunes
        if start.weekday() != 0:
            raise ValidationError("La fecha debe ser un lunes.")
        # 2) Validar duplicado
        if Week.objects.filter(start_day=start).exists():
            raise ValidationError("Ya existe una semana con esa fecha de inicio.")
        return start
