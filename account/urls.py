from django.urls import path

from . import views

urlpatterns = [
    path('checkIs', views.checkIs, name='checkIs'),
    path('saveAccount', views.save_account, name='saveAccount'),
]

