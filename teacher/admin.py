from django.contrib import admin
from .models import *


# Register your models here.
class Teacher_list(admin.ModelAdmin):
    list_display = ('name', 'sex', 'tell', 'address', 'college', 'profession')
    list_max_show_all = 5
    list_per_page = 5
    search_fields = ['name']
    exclude = ['department', ]
    ordering = ('name', 'sex', 'tell', 'address', 'college', 'profession')
    list_display_links = ('name',)


class College_list(admin.ModelAdmin):
    list_display = ('name', 'detail')
    list_max_show_all = 5
    list_per_page = 5
    search_fields = ['name']
    ordering = ('name', 'detail')
    list_display_links = ('name', )


class Department_list(admin.ModelAdmin):
    list_display = ('name', 'detail')
    list_max_show_all = 5
    list_per_page = 5
    search_fields = ['name']
    ordering = ('name', 'detail')
    list_display_links = ('name', )


class Profession_list(admin.ModelAdmin):
    list_display = ('name', 'detail')
    list_max_show_all = 5
    list_per_page = 5
    search_fields = ['name']
    ordering = ('name', 'detail')
    list_display_links = ('name', )


admin.site.register(Teacher, Teacher_list)
admin.site.register(College, College_list)
admin.site.register(Department, Department_list)
admin.site.register(Profession, Profession_list)
