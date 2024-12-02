from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from otonevrolog_main.accounts.models import CustomUser
from otonevrolog_main.web.models import AppointmentResult


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

        self.assertEqual(response.status_code, 302)  # Проверка за redirect
        self.assertRedirects(response, reverse('index'))  # Уверява се, че редиректът е правилен
        self.assertEqual(CustomUser.objects.count(), 1)  # Проверява създаването на потребителя
        self.assertTrue(
            CustomUser.objects.filter(username='testuser').exists())  # Проверява съществуването на потребителя

    def test_register_user_invalid_data(self):
        form_data = {
            'username': 'testuser',
            'password1': 'password123',
            'password2': 'differentpassword',  # Различни пароли
        }
        response = self.client.post(self.register_url, form_data)

        self.assertEqual(response.status_code, 200)  # Остава на страницата
        self.assertTemplateUsed(response, 'registration/register.html')  # Проверява използвания темплейт
        self.assertEqual(CustomUser.objects.count(), 0)  # Не е създаден потребител

    def test_register_user_get_request(self):
        response = self.client.get(self.register_url)

        self.assertEqual(response.status_code, 200)  # Успешен GET
        self.assertTemplateUsed(response, 'registration/register.html')  # Проверка за правилен темплейт

