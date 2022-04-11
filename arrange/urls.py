from django.urls import path
from . import views
urlpatterns = [
    # path('', views,),
    path('getMessage', views.getMessage, name="getMessage"),
    path('confirmArrange', views.confirmArrange, name="confirmArrange"),
    path('refuseArrange', views.refuseArrange, name="refuseArrange"),
    path('arrangeExam', views.arrangeExam, name="arrangeExam"),
]
