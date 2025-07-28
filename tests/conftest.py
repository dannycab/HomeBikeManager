import pytest
from app import app, db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        # Optionally, clean up DB after tests
        with app.app_context():
            db.drop_all()
