from django.contrib.auth.views import LoginView
from django.urls import path

from .views import UserCreateView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user-register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='user-login')
]
