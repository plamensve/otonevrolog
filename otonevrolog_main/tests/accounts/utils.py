from django.test import TestCase

from otonevrolog_main.accounts.models import CustomUser
from otonevrolog_main.accounts.utils import get_current_user


class GetCurrentUserTest(TestCase):
    def setUp(self):
        self.user1 = CustomUser.objects.create_user(username='user1', password='password1')
        self.user2 = CustomUser.objects.create_user(username='user2', password='password2')

    def test_get_current_user_valid_pk(self):
        retrieved_user = get_current_user(self.user1.pk)
        self.assertEqual(retrieved_user, self.user1)
        self.assertEqual(retrieved_user.username, 'user1')

