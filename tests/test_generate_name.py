import random

from fastapi.testclient import TestClient

from api.main import app

def test_generate_name():
    with TestClient(app) as client:
        random.seed(123)
        response = client.get("/generate_name")
        assert response.status_code == 200
        assert response.json() == {"name": "Minnie"}

def test_generate_name_max_len():
    with TestClient(app) as client:
        random.seed(123)
        response = client.get("/generate_name?max_len=5")
        assert response.status_code == 200
        assert response.json() == {"name": "Noa"}

def test_generate_name_starts_with():
    with TestClient(app) as client:
        random.seed(123)
        response = client.get("/generate_name?starts_with=M")
        assert response.status_code == 200
        assert response.json() == {"name": "Minnie"}

def test_generate_name_no_names_found():
    with TestClient(app) as client:
        random.seed(123)
        response = client.get("/generate_name?starts_with=Z")
        assert response.status_code == 404
        assert response.json() == {"detail": "No matching names"}