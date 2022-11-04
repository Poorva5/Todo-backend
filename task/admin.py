from django.contrib import admin
from .models import TaskData

@admin.register(TaskData)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "completed", "user"]
