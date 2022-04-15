from django.contrib import admin
from .models import *


# Register your models here.

class Exam_list(admin.ModelAdmin):
    list_display = ('course', 'detail', 'date', 'time_length', 'person', 'semesters')
    list_max_show_all = 5
    list_per_page = 5
    search_fields = ['course', 'detail']
    ordering = ('course', 'detail', 'date', 'time_length', 'person', 'semesters')
    # form = Account_form
    exclude = ['address', ]
    # fields = ('nick', 'account', 'wx_uid')
    List_display_links = ()

    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return False

    # def save_model(self, request, obj, form, change):
    #     # 取消后台编辑附件功能
    #     return False
    def has_add_permission(self, request):
        # 禁用添加
        return False

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['date', 'time_length', 'person', 'semesters', 'collage']
        else:
            return []

class Arrange_list(admin.ModelAdmin):
    list_display = ('teacher_account', 'exam_id', 'invigilate')
    list_max_show_all = 5
    # search_fields = ['teacher_account']
    list_per_page = 5
    ordering = ('teacher_account', 'exam_id')
    # form = Account_form
    # exclude = ['id', ]
    # fields = ('nick', 'account', 'wx_uid')
    List_display_links = ()

    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return False

    # def save_model(self, request, obj, form, change):
    #     # 取消后台编辑附件功能
    #     return False
    def has_add_permission(self, request):
        # 禁用添加
        return False

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['teacher_account', 'exam_id', 'invigilate_state', 'add_date']
        else:
            return []


admin.site.register(Exam, Exam_list)
admin.site.register(Arrange, Arrange_list)


