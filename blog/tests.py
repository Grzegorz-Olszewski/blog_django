from django.test import TestCase
from django.urls import reverse

from .models import Post
from .views import PostListView


class PostTest(TestCase):
    def create_post(self, title='title', content='content'):
        return Post.objects.create(title=title, content=content)

    def test_post_creation(self):
        post = self.create_post()
        self.assertTrue(isinstance(post, Post))
        self.assertTrue('title' == post.title)

    def test_get_absolute_url_for_post(self):
        post = self.create_post()
        expected_url = '/post/1/'
        self.assertEquals(post.get_absolute_url(), expected_url)

    def test_post_list_view(self):
        post = self.create_post()
        url = reverse('blog:index')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(post.title, str(resp.content))

    def test_post_list_view_no_posts(self):
        url = reverse('blog:index')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn("No posts available.", str(resp.content))

    def test_post_detail_view(self):
        post = self.create_post()
        url = reverse('blog:details_post', args=[post.id])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(post.title, str(resp.content))

    def test_post_create_view(self):
        url = reverse('blog:create_post',
                      kwargs={'title':'title', 'content':'content'})
        resp = self.client.post(url)
        self.assertEqual(resp.status_code, 204)


