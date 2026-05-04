import pytest
import sys, os

# Ensure Python can find ACEest_Fitness.py in parent folder
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ACEest_Fitness import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to ACEest Fitness" in response.data

def test_login_page(client):
    response = client.get('/login')
    assert response.status_code == 200
    assert b"Login Page" in response.data

def test_members_page(client):
    response = client.get('/members')
    assert response.status_code == 200
    assert b"Members List" in response.data

def test_classes_page(client):
    response = client.get('/classes')
    assert response.status_code == 200
    assert b"Classes Schedule" in response.data

def test_trainers_page(client):
    response = client.get('/trainers')
    assert response.status_code == 200
    assert b"Trainer Profiles" in response.data

def test_invalid_route(client):
    response = client.get('/nonexistent')
    assert response.status_code == 404
