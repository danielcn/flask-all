import unittest
from unittest.mock import patch
from flask import request

from app import app

class TestApi(unittest.TestCase):
    def test_index_status_200(self):
        with app.test_client() as client:
            response = client.get("/")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data, b'status 200 index')

    def test_index_with_return(self):
        with app.test_client() as client:
            response = client.get('/error')

            self.assertEqual(response.status_code, 500)
            self.assertEqual(response.data, b'status 500 error')

    def test_index_status_200_with_parameter(self):
        with app.test_client() as client:
            response = client.get('/?ready=true')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(request.args['ready'], 'true')
