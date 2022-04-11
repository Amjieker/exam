from django.contrib import admin
from .models import *


# Register your models here.


class Account_list(admin.ModelAdmin):
    list_display = ('nick', 'account')
    list_max_show_all = 5
    list_per_page = 5
    search_fields = ['nick']
    ordering = ('nick', 'account')
    # form = Account_form
    exclude = ['password', ]
    # fields = ('nick', 'account', 'wx_uid')
    List_display_links = ()

    def has_delete_permission(self, request, obj=None):
        # 禁用删除按钮
        return False

    # def save_model(self, request, obj, form, change):
    #     # 取消后台编辑附件功能
    #     return False

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["account", "wx_uid"]
        else:
            return []


admin.site.register(Account, Account_list)
