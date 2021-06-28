from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	
    path('register',views.register),
    path('login',views.login),
    path('logout',views.logout),
    path('books',views.fav_books), # show the second html page
    path('favorite_book/add',views.add_book),
    path('books/<int:id>/favorite',views.fav_book),
    path('books/<int:id>/unfavorite',views.unfav_book),
    path('books/<int:id>',views.fav_book_info),
    path('recipes/<int:id>/update',views.update),
    path('books/<int:id>/delete',views.delete_book),

]
