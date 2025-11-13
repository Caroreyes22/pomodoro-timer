from django.urls import path
from . import views

urlpatterns = [
    path('', views.timer, name='home'), 
    path('timer/', views.timer, name='timer'),
    path('tips/', views.consejos, name='consejos'), 
]