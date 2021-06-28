from django.urls import path, include           # import include
urlpatterns = [
    path('', include('great_number_game_app.urls')),	   
]
