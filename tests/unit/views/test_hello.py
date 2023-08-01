import unittest

from rh_ui.app import create_app


class TestHelloWorld(unittest.TestCase):

    def test_cookies_success(self):
        test_app = create_app()
        test_client = test_app.test_client()

        response = test_client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertTrue("<title>Title: Hello World!</title>".encode() in response.data)
        self.assertTrue("<h1>Hello World!</h1>".encode() in response.data)
