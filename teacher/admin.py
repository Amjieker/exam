from django.contrib import admin
from .models import *


# Register your models here.
class Teacher_list(admin.ModelAdmin):
    list_display = ('id', 'name', 'sex', 'tell', 'address', 'college', 'department', 'profession')
    list_max_show_all = 5
    list_per_page = 5
    search_fields = ['id', 'name']
    ordering = ('id', 'name', 'sex', 'tell', 'address', 'college', 'department', 'profession')
    list_display_links = ('id', 'name')


class College_list(admin.ModelAdmin):
    list_display = ('id', 'name', 'detail')
    list_max_show_all = 5
    list_per_page = 5
    search_fields = ['id', 'name']
    ordering = ('id', 'name', 'detail')
    list_display_links = ('id', 'name')


class Department_list(admin.ModelAdmin):
    list_display = ('id', 'name', 'detail')
    list_max_show_all = 5
    list_per_page = 5
    search_fields = ['id', 'name']
    ordering = ('id', 'name', 'detail')
    list_display_links = ('id', 'name')


class Profession_list(admin.ModelAdmin):
    list_display = ('id', 'name', 'detail')
    list_max_show_all = 5
    list_per_page = 5
    search_fields = ['id', 'name']
    ordering = ('id', 'name', 'detail')
    list_display_links = ('id', 'name')


admin.site.register(Teacher, Teacher_list)
admin.site.register(College, College_list)
admin.site.register(Department, Department_list)
admin.site.register(Profession, Profession_list)
