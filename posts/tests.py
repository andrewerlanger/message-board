from django.test import TestCase
from django.urls import reverse

from .models import Post

# Create your tests here.

class CreateData(TestCase):

  def setUp(self):
    Post.objects.create(text="test post")

class PostModelTest(CreateData):

  def test_text_content(self):
    post = Post.objects.first()
    self.assertEqual(post.text, "test post")

class HomePageViewTest(CreateData):

  def test_view_url_exists_at_proper_location(self):
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)

  def test_view_url_by_name(self):
    response = self.client.get(reverse('home'))
    self.assertEqual(response.status_code, 200)

  def test_view_uses_correct_template(self):
    response = self.client.get(reverse('home'))

    # useful assertion for checking a certain template was used
    self.assertTemplateUsed(response, 'home.html')

