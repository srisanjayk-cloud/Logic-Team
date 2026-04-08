from django.contrib import admin

# Register your models here.

from .models import Event, Project

admin.site.register(Event)
admin.site.register(Project)
