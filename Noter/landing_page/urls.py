from django.urls import path
from . import views
from .views import landing_page

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
]