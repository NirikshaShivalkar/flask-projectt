import pytest
import sys
import os
import flask

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app  # Now it should find 'app.py'


@pytest.fixture
def client():
    app.config["TESTING"] = True
    client = app.test_client()
    yield client

def test_homepage(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"To-Do List" in response.data  # Check if "To-Do List" is in response

def test_add_task(client):
    response = client.post("/add", data={"task": "Buy groceries"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Buy groceries" in response.data

def test_delete_task(client):
    client.post("/add", data={"task": "Test Task"}, follow_redirects=True)
    response = client.get("/delete/1", follow_redirects=True)  # Assuming ID = 1
    assert response.status_code == 200
    assert b"Test Task" not in response.data
