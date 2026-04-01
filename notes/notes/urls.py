from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_user', views.create_user, name='create_user'),
    path('logout', views.logout_view, name='logout'),
    path('login', views.login_view, name='login'),
    path('create_note', views.create_note, name='create_note'),
    path('my_notes', views.my_notes, name='my_notes'),
    path('edit_note/<int:note_id>', views.edit_note, name='edit_note'),
    path('public_notes', views.public_notes, name='public_notes'),
    path('delete_note/<int:note_id>', views.delete_note, name='delete_note'),
]