from . import views
from django.urls import path

urlpatterns = [
   path('mywork',views.mywork,name='mywork'),
]