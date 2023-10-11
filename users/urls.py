from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import UserCreateView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user-register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='user-login'),
    path('logout/', LogoutView.as_view(), name='user-logout')
]
