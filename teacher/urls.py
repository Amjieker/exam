from django.urls import path
from . import views

urlpatterns = [
    path('college', views.get_College, name="college"),
    path('updateInfo', views.update, name="update"),
    path('', views.test, name="test"),
]
