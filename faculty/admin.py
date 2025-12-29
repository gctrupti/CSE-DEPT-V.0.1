from django.contrib import admin
from .models import Faculty
# Register your models here.

# admin.site.register(Faculty)

@admin.register(Faculty)                    # Custom admin for Faculty model            
class FacultyAdmin(admin.ModelAdmin):
    list_display = ("name", "designation", "department", "is_active")
    list_filter = ("department", "is_active")
    search_fields = ("name", "designation")
