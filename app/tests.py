from django.test import TestCase

from views import index


# Create your tests here.
class TestView(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
