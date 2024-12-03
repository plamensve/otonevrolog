from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from otonevrolog_main.accounts.forms import CustomAuthenticationForm
from otonevrolog_main.accounts.models import CustomUser


class RegisterViewTest(TestCase):
    def setUp(self):
        self.register_url = reverse('register')

    def test_register_user_valid_data(self):
        form_data = {
            'username': 'testuser',
            'password1': 'securepassword123',
            'password2': 'securepassword123',
        }
        response = self.client.post(self.register_url, form_data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertTrue(
            CustomUser.objects.filter(username='testuser').exists())

    def test_register_user_invalid_data(self):
        form_data = {
            'username': 'testuser',
            'password1': 'password123',
            'password2': 'differentpassword',
        }
        response = self.client.post(self.register_url, form_data)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')
        self.assertEqual(CustomUser.objects.count(), 0)

    def test_register_user_get_request(self):
        response = self.client.get(self.register_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')


class CustomLoginViewTest(TestCase):
    def setUp(self):
        # Създаване на тестов потребител
        self.user = CustomUser.objects.create_user(username='testuser', password='testpassword')
        self.login_url = reverse('login')

    def test_login_view_renders_correct_template(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_login_view_uses_custom_form(self):
        response = self.client.get(self.login_url)
        self.assertIsInstance(response.context['form'], CustomAuthenticationForm)

    def test_successful_login(self):
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertRedirects(response, reverse('index'))

    def test_unsuccessful_login(self):
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please enter a correct username and password.')
