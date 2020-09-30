import secrets
import unittest import patch

class TestApi(unittest.TestCase):
    @patch('secrets', return_value=expected_token)
    def test_generate_unique_link(self):
        token_url_safe = secrets.token_urlsafe()
        self.assertEqual(token_urlsafe, expected_toeken)
