from django.contrib import admin
from .models import Journey
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Journey)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('name', 'type', 'date', 'time_slots', 'price', 'seats_required', 'payment_type', 'requests')
    search_fields = ['name', 'type', 'date' 'seats_required', 'requests']
    list_filter = ('type',)
    prepopulated_fields = {'type': ('name',)}
    summernote_fields = ('content',)

# Register your models here.
