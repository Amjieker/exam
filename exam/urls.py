"""
项目 考试安排系统

"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('exam/', include('operate.urls')),
    path('teacher/', include('teacher.urls')),
    path('account/', include('account.urls')),
    path('arrange/', include('arrange.urls')),
    url(r'^static/(?P<path>.*)$', static.serve,
        {'document_root': settings.STATIC_ROOT}, name='static')
]

# config
admin.site.site_title = '管理平台'
admin.site.site_header = "SUSE考务管理系统"
