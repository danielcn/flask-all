import unittest
from unittest.mock import patch
from flask import request

from app import app

class TestApi(unittest.TestCase):
    def test_index_status_200(self):
        with app.test_client() as client:
            response = client.get("/")
            self.assertEqual(response.status_code, 200)


    def test_submit_return_message(self):
        with app.test_client() as client:
            response = client.get('/submit')
            self.assertEqual(response.data, send_mail("Messagge: {}".format(message)))
            
    
    def test_index_with_parameter(self):
        with app.test_client() as client:
            response = client.get('/?age=42')
            self.assertEqual(request.args['age'], '42')
            
    