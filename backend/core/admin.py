from django.contrib import admin
from .models import BuildProject, BuildTask, Material

@admin.register(BuildProject)
class BuildProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "client", "location", "budget", "spent", "created_at"]
    list_filter = ["status"]
    search_fields = ["name", "client", "location"]

@admin.register(BuildTask)
class BuildTaskAdmin(admin.ModelAdmin):
    list_display = ["title", "project_name", "assigned_to", "status", "priority", "created_at"]
    list_filter = ["status", "priority"]
    search_fields = ["title", "project_name", "assigned_to"]

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "quantity", "unit", "unit_cost", "created_at"]
    list_filter = ["category", "status"]
    search_fields = ["name", "unit", "supplier"]
