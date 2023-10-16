from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import FormMixin

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
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        # Here, we would record the user's interest using the message
        # passed in form.cleaned_data['message']
        return super(ImageDetailView, self).form_valid(form)
