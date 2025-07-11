from django.test import TestCase

class HomeTest(TestCase):
    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"Hello, CI/CD with Django!")
