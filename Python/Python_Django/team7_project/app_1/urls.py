from django.urls import path     
from . import views
from django.conf.urls.static import static
from team7_project import settings
urlpatterns = [
    path('', views.home),
    path('reg', views.registration),
    path('log', views.login),
    path('logOut', views.logOut),
    path('home',views.success),
    path('home/new',views.add_post),
    path('new',views.new),
    path('delete/<int:postId>',views.delete_post),
    path('show/<int:postId>',views.show_post),
    path('edit/<int:postId>',views.edit_post),
    path('add_comm/<int:postId>',views.add_comment),
    path('make_edit/<int:postId>',views.make_edit),
    path('like/<int:postId>',views.like),
    path('unlike/<int:postId>',views.unlike),
    path('profile',views.profile),
    path('home',views.search),
    path('show/<str:cats>',views.show_category),
    path('contact',views.contact),
    path('about',views.about),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)