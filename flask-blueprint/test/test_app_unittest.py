import unittest
from unittest.mock import patch
from flask import request

from app import app

class TestApi(unittest.TestCase):
    def test_index_status_200(self):
        with app.test_client() as client:
            response = client.get("/")
            self.assertEqual(response.status_code, 200)

    def test_index_with_return(self):
        with app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.data, b'Hello, world!')
    
    def test_index_with_parameter(self):
        with app.test_client() as client:
            response = client.get('/?age=42')
            self.assertEqual(request.args['age'], '42')
            
    