from django.urls import path

from .views import ImageCreateView

urlpatterns = [
    path('new/', ImageCreateView.as_view(), name='image-create'),
]
