from django.views.generic import CreateView

from .models import Image


class ImageCreateView(CreateView):
    model = Image
    template_name = 'imagebook/image_create.html'
    fields = ['title', 'image']
