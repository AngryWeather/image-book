from django.contrib.auth.models import User
from django.test import TestCase


class TestImageFormCreation(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='TestUser',
            email='TestEmail@email.com',
            password='password321'
        )

    def test_200_for_logged_in_user(self):
        self.client.login(username='TestUser', password='password321')
        form_data = {
            'title': 'Test Title',
            'image': 'test.jpg',
        }

        response = self.client.post('/image/new/', data=form_data)
        self.assertEqual(response.status_code, 200)

    def test_302_for_anonymous_user(self):
        form_data = {
            'title': 'Test Title',
            'image': 'test.jpg',
        }

        response = self.client.post('/image/new/', data=form_data)
        self.assertEqual(response.status_code, 302)
