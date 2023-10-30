from . import views
from django.urls import path

urlpatterns = [
   path('',views.demo,name='demo'),

    #path('content/',views.demo3,name='demo3'),
    #path('final/',views.demo4,name='demo4')
]