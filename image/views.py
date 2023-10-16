from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView

from .models import Image


class ImageCreateView(LoginRequiredMixin, CreateView):
    model = Image
    template_name = 'image/image_create.html'
    fields = ['title', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ImageListView(ListView):
    model = Image
    ordering = ['-date_posted']


class ImageDetailView(DetailView):
    model = Image
