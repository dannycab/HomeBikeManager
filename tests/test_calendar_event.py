import pytest
from app import app, db

def register_and_login(client, username='testuser', password='testpass'):
    client.post('/api/register', json={'username': username, 'password': password})
    login_resp = client.post('/api/login', json={'username': username, 'password': password})
    token = login_resp.get_json()['access_token']
    return {'Authorization': f'Bearer {token}'}

def test_create_event_valid(client):
    headers = register_and_login(client)
    # Create a bike for FK
    bike_resp = client.post('/api/bikes', json={
        'name': 'Event Bike',
        'brand': 'BrandX',
        'type': 'MTB',
        'purchase_date': '2025-07-20'
    }, headers=headers)
    bike_id = bike_resp.get_json()['id']
    # Create event
    resp = client.post('/api/calendar', json={
        'title': 'Test Event',
        'event_type': 'ride',
        'date': '2025-07-21',
        'notes': 'Test event notes',
        'bike_id': bike_id,
        'recurrence': 'weekly',
        'timezone': 'UTC',
        'public': True
    }, headers=headers)
    assert resp.status_code == 201
    data = resp.get_json()
    assert 'id' in data

def test_create_event_missing_fields(client):
    headers = register_and_login(client)
    resp = client.post('/api/calendar', json={
        'event_type': 'ride',
        'date': '2025-07-21'
    }, headers=headers)
    assert resp.status_code == 400
    assert 'error' in resp.get_json()

def test_get_event(client):
    headers = register_and_login(client)
    # Create event
    resp = client.post('/api/calendar', json={
        'title': 'Get Event',
        'event_type': 'maintenance',
        'date': '2025-07-22',
        'notes': 'Get event notes',
        'public': False
    }, headers=headers)
    event_id = resp.get_json()['id']
    # Get event
    get_resp = client.get(f'/api/calendar/{event_id}', headers=headers)
    assert get_resp.status_code == 200
    data = get_resp.get_json()
    assert data['title'] == 'Get Event'
    assert data['event_type'] == 'maintenance'

def test_update_event(client):
    headers = register_and_login(client)
    # Create event
    resp = client.post('/api/calendar', json={
        'title': 'Update Event',
        'event_type': 'race',
        'date': '2025-07-23',
        'public': False
    }, headers=headers)
    event_id = resp.get_json()['id']
    # Update event
    update_resp = client.put(f'/api/calendar/{event_id}', json={
        'title': 'Updated Event',
        'public': True
    }, headers=headers)
    assert update_resp.status_code == 200
    # Get event and check update
    get_resp = client.get(f'/api/calendar/{event_id}', headers=headers)
    assert get_resp.get_json()['title'] == 'Updated Event'
    assert get_resp.get_json()['public'] is True

def test_delete_event(client):
    headers = register_and_login(client)
    # Create event
    resp = client.post('/api/calendar', json={
        'title': 'Delete Event',
        'event_type': 'ride',
        'date': '2025-07-24',
        'public': False
    }, headers=headers)
    event_id = resp.get_json()['id']
    # Delete event
    del_resp = client.delete(f'/api/calendar/{event_id}', headers=headers)
    assert del_resp.status_code == 200
    # Try to get deleted event
    get_resp = client.get(f'/api/calendar/{event_id}', headers=headers)
    assert get_resp.status_code == 404

def test_event_permissions(client):
    headers1 = register_and_login(client, 'user1', 'pass1')
    headers2 = register_and_login(client, 'user2', 'pass2')
    # user1 creates private event
    resp = client.post('/api/calendar', json={
        'title': 'Private Event',
        'event_type': 'ride',
        'date': '2025-07-25',
        'public': False
    }, headers=headers1)
    event_id = resp.get_json()['id']
    # user2 tries to get user1's private event
    get_resp = client.get(f'/api/calendar/{event_id}', headers=headers2)
    assert get_resp.status_code == 404
    # user2 tries to delete user1's event
    del_resp = client.delete(f'/api/calendar/{event_id}', headers=headers2)
    assert del_resp.status_code == 403
    # user1 deletes own event
    del_resp2 = client.delete(f'/api/calendar/{event_id}', headers=headers1)
    assert del_resp2.status_code == 200
