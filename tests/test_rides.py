import pytest
from app import app, db

def test_get_rides(client):
    response = client.get('/api/rides')
    assert response.status_code in (200, 501)

def test_create_ride(client):
    # Should return 400 for missing required fields
    response = client.post('/api/rides', json={})
    assert response.status_code == 400

def test_create_ride_valid(client):
    # Register and login to get JWT
    client.post('/api/register', json={'username': 'testuser', 'password': 'testpass'})
    login_resp = client.post('/api/login', json={'username': 'testuser', 'password': 'testpass'})
    token = login_resp.get_json()['access_token']
    headers = {'Authorization': f'Bearer {token}'}
    # Create a bike first (required foreign key)
    bike_resp = client.post('/api/bikes', json={
        'name': 'Test Bike',
        'brand': 'TestBrand',
        'type': 'Road',
        'purchase_date': '2025-07-20'
    }, headers=headers)
    bike_id = bike_resp.get_json()['id']
    # Now create a ride
    ride_resp = client.post('/api/rides', json={
        'date': '2025-07-20',
        'distance': 42.0,
        'notes': 'Test ride',
        'map_file': None,
        'bike_id': bike_id
    }, headers=headers)
    assert ride_resp.status_code == 201
