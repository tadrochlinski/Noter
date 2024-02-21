from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('create/', views.create_note, name='create_note'),
    path('note/<slug:slug>/', views.view_note, name='view_note'),
    path('edit/<slug:slug>/', views.edit_note, name='edit_note'),
    path('delete/<slug:slug>/', views.delete_note, name='delete_note'),
]