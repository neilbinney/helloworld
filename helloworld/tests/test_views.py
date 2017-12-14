from django.test import TestCase
from helloworld import views
from django.core.urlresolvers import reverse
import os.path as path

class ViewsTestCase(TestCase):

  def test_welcome_view(self):
    """Index view is rendered correctly"""
    url = reverse('index')
    resp = self.client.get(url)

    self.assertEqual(resp.status_code, 200)
