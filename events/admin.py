from django.contrib import admin
from .models import Event
# Register your models here.

# admin.site.register(Event)

@admin.register(Event)                       # Custom admin for Event model
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "club", "date", "status")
    list_filter = ("status", "club", "date")
    search_fields = ("title", "club__name")
    ordering = ("-date",)
