from django.contrib.auth.models import User
from django.test import TestCase

from image.models import Image


class ImageModelTest(TestCase):

    def setUp(self):
        author = User.objects.create(username='TestUser', email='testuser@email.com', password='password321')
        Image.objects.create(title='Test Image', author=author, image='test.png')

    def test_get_absolute_url(self):
        image = Image.objects.get(id=1)
        self.assertEqual(image.get_absolute_url(), '/image/1/')
