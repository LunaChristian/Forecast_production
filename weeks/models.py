from django.db import models
# Create your models here.

class Week(models.Model):
    DRAFT = 'draft'
    CONFIRMED = 'confirmed'
    STATE_CHOICES = [
        (DRAFT, 'Borrador'),
        (CONFIRMED, 'Confirmada'),
    ]

    start_date = models.DateField(unique=True, help_text="Fecha del lunes que inicia la semana")
    state = models.CharField(max_length=10, choices=STATE_CHOICES, default=DRAFT, help_text="Estado de la semana")

    class Meta:
        ordering = ['-start_date']
        verbose_name = "Semana"
        verbose_name_plural = "Semanas"

    def __str__(self):
        return f"Semana {self.start_date:%d/%m/%Y} ({self.get_state_display()})"
    
class DayEntry(models.Model):
    LISTA_DIAS = [
        (0, 'Lunes'),
        (1, 'Martes'),
        (2, 'Miercoles'),
        (3, 'Jueves'),
        (4, 'Viernes'),
        (5, 'Sabado'),
        (6, 'Domingo'),
    ]

    week = models.ForeignKey('Week', related_name='days', on_delete=models.CASCADE)
    weekday = models.IntegerField(choices=LISTA_DIAS)
    estimated_pizzas = models.PositiveIntegerField(default=0, verbose_name='Cantidad')
    
    class Meta:
        unique_together = ('week', 'weekday')
        ordering = ['weekday']
        verbose_name = 'Registro diario'
        verbose_name_plural = 'Registros diarios'
    
    def __str__(self):
        return f"{self.get_weekday_display()}: {self.estimated_pizzas} pizzas"