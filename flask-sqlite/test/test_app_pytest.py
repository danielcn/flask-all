from flask import request
from app import app

def test_index_status_200():
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
