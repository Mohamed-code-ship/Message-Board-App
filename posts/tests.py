from django.test import TestCase
from django.urls import reverse
# Create your tests here.
from .models import Post

class PostTestCase(TestCase):
    def setUp(self):
        Post.objects.create(text='just a text')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name,'just a text')

class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='this is another test')

    def test_url_exist_proper_location(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code,200)

    def test_view_url_by_name(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code,200)

    def test_view_uses_correct_template(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code,200)
        self.assertTemplateUsed(res,'home.html')
    