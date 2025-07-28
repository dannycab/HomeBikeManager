
import logging
from flask import Flask, request, jsonify, g
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from werkzeug.security import generate_password_hash, check_password_hash
import secrets

from models.models import db, User, Bike, Part
import jwt
import os
from datetime import datetime, timedelta



# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

JWT_SECRET = os.environ.get('JWT_SECRET', 'changeme-please-set-in-.env')
JWT_ALGO = 'HS256'

def create_jwt(username: str) -> str:
    payload = {
        'sub': username,
        'exp': datetime.utcnow() + timedelta(days=7)
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGO)

def decode_jwt(token: str):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGO])
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def require_jwt(func):
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization', '')
        if not auth_header.startswith('Bearer '):
            logger.warning('Missing or invalid Authorization header')
            return jsonify({'error': 'Authorization header required'}), 401
        token = auth_header.split(' ', 1)[1]
        user = decode_jwt(token)
        if not user:
            logger.warning('Invalid or expired JWT')
            return jsonify({'error': 'Invalid or expired token'}), 401
        g.current_user = user
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper


from frontend import frontend

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///homebikemanager.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret')
db.init_app(app)
api = Api(app)
app.register_blueprint(frontend)



@app.route('/')
def index():
    logger.info('Root endpoint accessed')
    return {'message': 'Welcome to HomeBikeManager API!'}

# --- Auth Endpoints ---
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        logger.warning('Registration failed: missing username or password')
        return jsonify({'error': 'Username and password required'}), 400
    if User.query.filter_by(username=username).first():
        logger.warning('Registration failed: username already exists')
        return jsonify({'error': 'Username already exists'}), 400
    user = User(
        username,
        generate_password_hash(password),
        data.get('is_admin', False)
    )
    db.session.add(user)
    db.session.commit()
    logger.info(f'User registered: {username}')
    return jsonify({'message': 'User registered successfully'})


@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password_hash, password):
        token = create_jwt(username)
        logger.info(f'User logged in: {username}')
        return jsonify({'access_token': token})
    logger.warning(f'Login failed for user: {username}')
    return jsonify({'error': 'Invalid credentials'}), 401

# --- Bike Endpoints ---
class BikeListResource(Resource):
    method_decorators = [require_jwt]
    def get(self):
        bikes = Bike.query.all()
        logger.info('Listing bikes')
        return [
            {'id': b.id, 'name': b.name, 'brand': b.brand, 'type': b.type, 'purchase_date': b.purchase_date.isoformat() if b.purchase_date else None}
            for b in bikes
        ]
    def post(self):
        from datetime import datetime
        data = request.get_json()
        purchase_date = data.get('purchase_date')
        if purchase_date:
            try:
                purchase_date = datetime.strptime(purchase_date, "%Y-%m-%d").date()
            except Exception:
                return {'error': 'Invalid purchase_date format, use YYYY-MM-DD'}, 400
        bike = Bike(
            data['name'],
            data['brand'],
            data['type'],
            purchase_date
        )
        db.session.add(bike)
        db.session.commit()
        logger.info(f'Bike created: {bike.name}')
        return {'id': bike.id}, 201

class BikeResource(Resource):
    method_decorators = [require_jwt]
    def get(self, bike_id):
        bike = Bike.query.get_or_404(bike_id)
        logger.info(f'Get bike: {bike_id}')
        return {'id': bike.id, 'name': bike.name, 'brand': bike.brand, 'type': bike.type, 'purchase_date': bike.purchase_date.isoformat() if bike.purchase_date else None}
    def put(self, bike_id):
        from datetime import datetime
        bike = Bike.query.get_or_404(bike_id)
        data = request.get_json()
        bike.name = data.get('name', bike.name)
        bike.brand = data.get('brand', bike.brand)
        bike.type = data.get('type', bike.type)
        purchase_date = data.get('purchase_date')
        if purchase_date:
            try:
                purchase_date = datetime.strptime(purchase_date, "%Y-%m-%d").date()
            except Exception:
                return {'error': 'Invalid purchase_date format, use YYYY-MM-DD'}, 400
            bike.purchase_date = purchase_date
        db.session.commit()
        logger.info(f'Bike updated: {bike_id}')
        return {'message': 'Bike updated'}
    def delete(self, bike_id):
        bike = Bike.query.get_or_404(bike_id)
        db.session.delete(bike)
        db.session.commit()
        logger.info(f'Bike deleted: {bike_id}')
        return {'message': 'Bike deleted'}

# --- Part Endpoints ---
class PartListResource(Resource):
    method_decorators = [require_jwt]
    def get(self):
        parts = Part.query.all()
        logger.info('Listing parts')
        return [
            {'id': p.id, 'name': p.name, 'type': p.type, 'install_date': p.install_date.isoformat() if p.install_date else None, 'bike_id': p.bike_id}
            for p in parts
        ]
    def post(self):
        from datetime import datetime
        data = request.get_json()
        install_date = data.get('install_date')
        if install_date:
            try:
                install_date = datetime.strptime(install_date, "%Y-%m-%d").date()
            except Exception:
                return {'error': 'Invalid install_date format, use YYYY-MM-DD'}, 400
        part = Part(
            data['name'],
            data['type'],
            install_date,
            data.get('bike_id')
        )
        db.session.add(part)
        db.session.commit()
        logger.info(f'Part created: {part.name}')
        return {'id': part.id}, 201

class PartResource(Resource):
    method_decorators = [require_jwt]
    def get(self, part_id):
        part = Part.query.get_or_404(part_id)
        logger.info(f'Get part: {part_id}')
        return {'id': part.id, 'name': part.name, 'type': part.type, 'install_date': part.install_date.isoformat() if part.install_date else None, 'bike_id': part.bike_id}
    def put(self, part_id):
        from datetime import datetime
        part = Part.query.get_or_404(part_id)
        data = request.get_json()
        part.name = data.get('name', part.name)
        part.type = data.get('type', part.type)
        install_date = data.get('install_date')
        if install_date:
            try:
                install_date = datetime.strptime(install_date, "%Y-%m-%d").date()
            except Exception:
                return {'error': 'Invalid install_date format, use YYYY-MM-DD'}, 400
            part.install_date = install_date
        part.bike_id = data.get('bike_id', part.bike_id)
        db.session.commit()
        logger.info(f'Part updated: {part_id}')
        return {'message': 'Part updated'}
    def delete(self, part_id):
        part = Part.query.get_or_404(part_id)
        db.session.delete(part)
        db.session.commit()
        logger.info(f'Part deleted: {part_id}')
        return {'message': 'Part deleted'}


# Register resources
api.add_resource(BikeListResource, '/api/bikes')
api.add_resource(BikeResource, '/api/bikes/<int:bike_id>')
api.add_resource(PartListResource, '/api/parts')
api.add_resource(PartResource, '/api/parts/<int:part_id>')

# --- New Feature Stubs ---
from resources.ride import RideResource
from resources.calendar_event import CalendarEventResource
from resources.upload import FileUploadResource
from resources.auth_jwt import JWTAuthResource

api.add_resource(RideResource, '/api/rides', '/api/rides/<int:ride_id>')
CalendarEventResource.method_decorators = [require_jwt]
api.add_resource(CalendarEventResource, '/api/calendar', '/api/calendar/<int:event_id>')
api.add_resource(FileUploadResource, '/api/rides/upload')
api.add_resource(JWTAuthResource, '/api/auth/jwt')

if __name__ == '__main__':
    import sys
    port = 5000
    # Allow port override via command-line or environment variable
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except Exception:
            pass
    import os
    port = int(os.environ.get('PORT', port))
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=port)