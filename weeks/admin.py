from django.contrib import admin
from .models import Week, DayEntry

# Register your models here.

@admin.register(Week)
class WeekAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'state')
    list_filter = ('state',)
    ordering = ('-start_date',)
    search_fields = ('start_date',)
    
@admin.register(DayEntry)
class DayEntryAdmin(admin.ModelAdmin):
    list_display = ('week', 'weekday', 'estimated_pizzas')
    list_filter = ('weekday',)
    ordering = ('week', 'weekday')