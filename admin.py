from django.contrib import admin
from .models import Module, Student, Registration

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'credit', 'category', 'availability']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['date_of_birth', 'address', 'city_town', 'country', 'photo']

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['student', 'module', 'date_of_registration']

