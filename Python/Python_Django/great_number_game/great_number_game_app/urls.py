from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	
    path('guess',views.process_guess),
    path('restart',views.newgame)
]
