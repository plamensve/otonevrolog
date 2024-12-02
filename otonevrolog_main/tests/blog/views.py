from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from otonevrolog_main.blog.forms import CommentForm
from otonevrolog_main.blog.models import BlogPost, Comment

CustomUser = get_user_model()


class BlogDetailViewTest(TestCase):
    def setUp(self):
        # Създаване на тестов потребител
        self.user = CustomUser.objects.create_user(username='testuser', password='password', first_name='Test',
                                                   last_name='User')
        # Създаване на тестов BlogPost
        self.blog_post = BlogPost.objects.create(title='Test Blog', content='Test content', author=self.user)

        # URL за view-то
        self.url = reverse('blog_detail', kwargs={'pk': self.blog_post.pk})

    def test_view_renders_correct_template(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_detail.html')

    def test_post_invalid_comment(self):
        self.client.login(username='testuser', password='password')

        form_data = {'content': ''}  # Невалидни данни
        response = self.client.post(self.url, form_data)

        # Проверка, че остава на същата страница
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_detail.html')

        # Проверка, че не е създаден коментар
        self.assertEqual(Comment.objects.count(), 0)
        self.assertTrue(response.context['form'].errors)

