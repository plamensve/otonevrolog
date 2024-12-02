from django.test import TestCase
from django.urls import reverse

from otonevrolog_main.accounts.models import CustomUser
from otonevrolog_main.web.models import Review


class IndexAndSubmitReviewTests(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', password='12345')
        self.index_url = reverse('index')
        self.submit_review_url = reverse('submit_review')

    def test_index_get_authenticated(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)

        self.assertIn('days_of_week', response.context)
        self.assertIn('hours', response.context)
        self.assertIn('form', response.context)
        self.assertIn('unavailable_slot', response.context)
        self.assertIn('comments', response.context)

    def test_index_get_no_auth(self):
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)

        for field in response.context['form'].fields.values():
            self.assertTrue(field.disabled)

    def test_submit_review_get_request(self):
        response = self.client.get(self.submit_review_url)
        self.assertEqual(response.status_code, 302)  # Redirect
