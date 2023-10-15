from django.urls import path

from .views import ImageCreateView, ImageDetailView

urlpatterns = [
    path('new/', ImageCreateView.as_view(), name='image-create'),
    path('<int:pk>/', ImageDetailView.as_view(), name='image-detail')
]
