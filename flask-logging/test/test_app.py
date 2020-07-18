import unittest
from unittest.mock import patch

from app import app

class TestApi(unittest.TestCase):
    def test_app_home(self):
        with app.test_client() as client:
            response = client.get("/")
            self.assertEqual(response.status_code, 200)