import os
import pytest
import requests

BASE_URL = os.environ.get("API_BASE_URL", "http://localhost:5000")
USERNAME = "apitestuser"
PASSWORD = "apitestpass"
API_KEY_FILE = "tests/api_key.txt"

@pytest.fixture(scope="session")
def api_key():
    # Register user (ignore if already exists)
    requests.post(f"{BASE_URL}/api/register", json={"username": USERNAME, "password": PASSWORD})
    # Login
    r = requests.post(f"{BASE_URL}/api/login", json={"username": USERNAME, "password": PASSWORD})
    assert r.status_code == 200
    key = r.json()["api_key"]
    with open(API_KEY_FILE, "w") as f:
        f.write(key)
    return key

def test_bikes(api_key):
    headers = {"X-API-KEY": api_key}
    # List bikes
    r = requests.get(f"{BASE_URL}/api/bikes", headers=headers)
    assert r.status_code == 200
    # Create bike
    bike_data = {"name": "TestBike", "brand": "TestBrand", "type": "TestType", "purchase_date": "2025-01-01"}
    r = requests.post(f"{BASE_URL}/api/bikes", headers=headers, json=bike_data)
    assert r.status_code == 201
    # List again
    r = requests.get(f"{BASE_URL}/api/bikes", headers=headers)
    assert r.status_code == 200
    assert any(b["name"] == "TestBike" for b in r.json())

def test_parts(api_key):
    headers = {"X-API-KEY": api_key}
    # List parts
    r = requests.get(f"{BASE_URL}/api/parts", headers=headers)
    assert r.status_code == 200
    # Create part (assume bike_id=1)
    part_data = {"name": "TestChain", "type": "Drivetrain", "install_date": "2025-07-20", "bike_id": 1}
    r = requests.post(f"{BASE_URL}/api/parts", headers=headers, json=part_data)
    assert r.status_code == 201
    # List again
    r = requests.get(f"{BASE_URL}/api/parts", headers=headers)
    assert r.status_code == 200
    assert any(p["name"] == "TestChain" for p in r.json())
