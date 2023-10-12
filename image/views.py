from django.views.generic import CreateView

from .models import Image


class ImageCreateView(CreateView):
    model = Image
    template_name = 'image/image_create.html'
    fields = ['title', 'image']
