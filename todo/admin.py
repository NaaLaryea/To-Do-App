from django.contrib import admin
from todo.models import Todo

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display=['user', 'task_name', 'task_desc', 'status', 'priority', 'due_date', 'date_created']

admin.site.register(Todo, TodoAdmin)