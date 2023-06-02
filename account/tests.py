from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import UserProfile

class UserProfileTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.profile = UserProfile.objects.create(user=self.user, name='Test User', gender='male', employee_type='teacher')

    def test_profile_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/profile.html')
        self.assertEqual(response.context['profile'], self.profile)

    def test_update_profile_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('update-profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/update-profile.html')
        self.assertEqual(response.context['forms'].instance, self.profile)

    def test_update_profile_form_submission(self):
        self.client.login(username='testuser', password='testpassword')
        data = {
            'name': 'Updated User',
            'photo': '/path/to/photo.jpg',
        }
        response = self.client.post(reverse('update-profile'), data=data)
        self.assertEqual(response.status_code, 200)
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.name, 'Updated User')
        self.assertEqual(self.profile.photo, '/path/to/photo.jpg')
