from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('partial', views.partial , name='partial'),
    path('processOne', views.processOne , name='processOne'),
]