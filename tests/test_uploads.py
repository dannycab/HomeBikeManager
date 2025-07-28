import io
import pytest
from app import app, db

def test_upload_gpx(client):
    # Register and login to get JWT
    client.post('/api/register', json={'username': 'uploaduser', 'password': 'uploadpass'})
    login_resp = client.post('/api/login', json={'username': 'uploaduser', 'password': 'uploadpass'})
    token = login_resp.get_json()['access_token']
    headers = {'Authorization': f'Bearer {token}'}
    # Upload a valid GPX file
    data = {
        'file': (io.BytesIO(b'<gpx></gpx>'), 'test.gpx')
    }
    resp = client.post('/api/rides/upload', content_type='multipart/form-data', data=data, headers=headers)
    assert resp.status_code == 201
    assert 'File uploaded' in resp.get_json()['message']

def test_upload_invalid_type(client):
    client.post('/api/register', json={'username': 'uploaduser2', 'password': 'uploadpass'})
    login_resp = client.post('/api/login', json={'username': 'uploaduser2', 'password': 'uploadpass'})
    token = login_resp.get_json()['access_token']
    headers = {'Authorization': f'Bearer {token}'}
    data = {
        'file': (io.BytesIO(b'not a gpx'), 'test.txt')
    }
    resp = client.post('/api/rides/upload', content_type='multipart/form-data', data=data, headers=headers)
    assert resp.status_code == 400
    assert 'Invalid file type' in resp.get_json()['error']
