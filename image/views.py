from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from .models import Image


class ImageCreateView(LoginRequiredMixin, CreateView):
    model = Image
    template_name = 'image/image_create.html'
    fields = ['title', 'image']
