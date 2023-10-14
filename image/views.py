from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from .models import Image


class ImageCreateView(LoginRequiredMixin, CreateView):
    model = Image
    template_name = 'image/image_create.html'
    fields = ['title', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
