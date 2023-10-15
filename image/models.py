from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Image(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images_posted')

    def get_absolute_url(self):
        return reverse('image-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=255)
    comment_image = models.ForeignKey(Image, on_delete=models.CASCADE)
