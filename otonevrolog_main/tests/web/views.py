from django.test import TestCase
from django.urls import reverse

from otonevrolog_main.accounts.models import CustomUser
from otonevrolog_main.web.models import AppointmentSlot


class IndexView(TestCase):
    def test_index_get(self):
        user = CustomUser.objects.create_user(username='testuser', password='12345')

        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

        self.assertIn('days_of_week', response.context)
        self.assertIn('hours', response.context)
        self.assertIn('form', response.context)
        self.assertIn('unavailable_slot', response.context)
        self.assertIn('comments', response.context)

    def test_index_get_no_auth(self):
        response = self.client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)

        for field in response.context['form'].fields.values():
            self.assertTrue(field.disabled)

