import logging
from flask import request, jsonify
from flask_restful import Resource
from models.models import db, Ride
from datetime import datetime

logger = logging.getLogger(__name__)

class RideResource(Resource):

    def get(self, ride_id=None):
        if ride_id:
            ride = Ride.query.get(ride_id)
            if not ride:
                logger.warning(f'Ride not found: {ride_id}')
                return {'error': 'Ride not found'}, 404
            return {
                'id': ride.id,
                'date': ride.date.isoformat(),
                'distance': ride.distance,
                'notes': ride.notes,
                'map_file': ride.map_file,
                'bike_id': ride.bike_id
            }
        rides = Ride.query.all()
        return [
            {
                'id': r.id,
                'date': r.date.isoformat(),
                'distance': r.distance,
                'notes': r.notes,
                'map_file': r.map_file,
                'bike_id': r.bike_id
            } for r in rides
        ]

    def post(self):
        data = request.get_json()
        try:
            date = data.get('date')
            if not date:
                return {'error': 'date is required (YYYY-MM-DD)'}, 400
            from datetime import datetime
            date_obj = datetime.strptime(date, "%Y-%m-%d").date()
            bike_id = data.get('bike_id')
            if not bike_id:
                return {'error': 'bike_id is required'}, 400
            ride = Ride(
                date_obj,
                data.get('distance'),
                data.get('notes'),
                data.get('map_file'),
                bike_id
            )
            db.session.add(ride)
            db.session.commit()
            logger.info(f'Ride created: {ride.id}')
            return {'id': ride.id}, 201
        except Exception as e:
            logger.error(f'Error creating ride: {e}')
            return {'error': 'Invalid input or server error'}, 400

    def put(self, ride_id):
        # TODO: Update ride
        return {'message': 'Ride update not yet implemented'}, 501

    def delete(self, ride_id):
        # TODO: Delete ride
        return {'message': 'Ride deletion not yet implemented'}, 501
