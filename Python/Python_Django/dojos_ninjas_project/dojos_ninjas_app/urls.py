from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	  
    path('dojo/create', views.add_dojo),
    path('ninja/create',views.add_ninja),
]

