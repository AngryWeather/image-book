from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Image(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images_posted')
