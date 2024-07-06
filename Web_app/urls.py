from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name='home'),
    path('list/',list,name='list')
]
