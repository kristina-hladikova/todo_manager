from django.contrib import admin
from todo_manager_app.models import Todo


class TodoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Todo, TodoAdmin)
