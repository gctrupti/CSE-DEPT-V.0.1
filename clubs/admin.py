from django.contrib import admin
from .models import Club, Activity
# Register your models here.

# admin.site.register(Club)
# admin.site.register(Activity)

@admin.register(Club)                         # Custom admin for Club model
class ClubAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)

@admin.register(Activity)                  # Custom admin for Activity model            
class ActivityAdmin(admin.ModelAdmin):
    list_display = ("title", "club", "date")
    list_filter = ("club", "date")
    search_fields = ("title", "club__name")
