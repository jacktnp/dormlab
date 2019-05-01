from django.contrib import admin

from .models import Employee, Guest

admin.site.register(Employee)
admin.site.register(Guest)