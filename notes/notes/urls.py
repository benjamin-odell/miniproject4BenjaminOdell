from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_user', views.create_user, name='create_user'),
    path('logout', views.logout_view, name='logout'),
    path('login', views.login_view, name='login'),
    path('create_note', views.create_note, name='create_note'),
]