
import pytest
from app import app, db
from tests.test_calendar_event import register_and_login

def test_get_events(client):
    headers = register_and_login(client)
    response = client.get('/api/calendar', headers=headers)
    assert response.status_code in (200, 501)

def test_create_event(client):
    headers = register_and_login(client)
    response = client.post('/api/calendar', json={}, headers=headers)
    assert response.status_code == 400
