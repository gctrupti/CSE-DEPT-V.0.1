from django.contrib import admin
from .models import InnovationContribution
# Register your models here.

# admin.site.register(InnovationContribution)

@admin.register(InnovationContribution)                      # Custom admin for InnovationContribution model
class InnovationContributionAdmin(admin.ModelAdmin):
    list_display = ("title", "faculty", "year")
    list_filter = ("year", "faculty")
    search_fields = ("title", "faculty__name")
