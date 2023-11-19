from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import FormMixin, UpdateView

from .forms import CreateCommentForm
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


class ImageDetailView(FormMixin, DetailView):
    model = Image
    form_class = CreateCommentForm

    def get_success_url(self):
        return reverse('image-detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(ImageDetailView, self).get_context_data(**kwargs)
        context['form'] = self.get_form()

        if not self.request.user.is_authenticated:
            context['form'].fields['content'].disabled = True
            context['form'].fields['content'].widget.attrs['placeholder'] = 'Log in to leave a comment'

        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        if form.is_valid():
            form.instance.comment_author = self.request.user
            form.instance.comment_image = self.object
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(ImageDetailView, self).form_valid(form)


class ImageUpdateView(UpdateView):
    model = Image
    fields = ['title', 'image']
