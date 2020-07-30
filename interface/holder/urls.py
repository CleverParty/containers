from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('partial', views.partial , name='partial'),
    path('processOne', views.processOne , name='processOne'),
    path('currentTime', views.currentTime , name='currentTime'),
    path('clickPush', views.clickPush , name='clickPush'),
    path('lychrel' , views.lychrel , name='lychrel')
]