from flask import request
from app import app

def test_index_status_200():
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200

def test_index_with_return():
    with app.test_client() as client:
        response = client.get('/')
        assert response.data == b'Hello, world!'

def test_index_with_parameter():
    with app.test_client() as client:
        rv = client.get('/?data=42')
        assert request.args['data'] == '42'
