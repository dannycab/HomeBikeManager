import logging
from flask import request
from flask_restful import Resource
from models.models import db, CalendarEvent
from datetime import datetime

logger = logging.getLogger(__name__)

class CalendarEventResource(Resource):

    def get(self, event_id=None):
        from flask import g
        user_id = getattr(g, 'current_user', None)
        if event_id:
            event = CalendarEvent.query.get(event_id)
            if not event or (event.user_id != user_id and not event.public):
                logger.warning(f'Event not found or not permitted: {event_id}')
                return {'error': 'Event not found'}, 404
            return self._serialize(event)
        events = CalendarEvent.query.filter((CalendarEvent.user_id == user_id) | (CalendarEvent.public == True)).all()
        return [self._serialize(e) for e in events]

    def post(self):
        from flask import g
        data = request.get_json()
        required = ['title', 'event_type', 'date']
        for field in required:
            if not data.get(field):
                return {'error': f'{field} is required'}, 400
        if data['event_type'] not in ('ride', 'maintenance', 'race'):
            return {'error': 'Invalid event_type'}, 400
        from datetime import datetime
        try:
            date_obj = datetime.strptime(data['date'], "%Y-%m-%d").date()
        except Exception:
            return {'error': 'Invalid date format, use YYYY-MM-DD'}, 400
        event = CalendarEvent(
            title=data['title'],
            event_type=data['event_type'],
            date=date_obj,
            notes=data.get('notes'),
            user_id=g.current_user,
            bike_id=data.get('bike_id'),
            part_id=data.get('part_id'),
            ride_id=data.get('ride_id'),
            recurrence=data.get('recurrence'),
            timezone=data.get('timezone'),
            public=bool(data.get('public', False))
        )
        db.session.add(event)
        db.session.commit()
        logger.info(f'Event created: {event.id}')
        return {'id': event.id}, 201

    def put(self, event_id):
        from flask import g
        event = CalendarEvent.query.get(event_id)
        if not event or event.user_id != g.current_user:
            return {'error': 'Not permitted'}, 403
        data = request.get_json()
        for field in ['title', 'event_type', 'date', 'notes', 'bike_id', 'part_id', 'ride_id', 'recurrence', 'timezone', 'public']:
            if field in data:
                setattr(event, field, data[field])
        db.session.commit()
        logger.info(f'Event updated: {event_id}')
        return {'message': 'Event updated'}

    def delete(self, event_id):
        from flask import g
        event = CalendarEvent.query.get(event_id)
        if not event or event.user_id != g.current_user:
            return {'error': 'Not permitted'}, 403
        db.session.delete(event)
        db.session.commit()
        logger.info(f'Event deleted: {event_id}')
        return {'message': 'Event deleted'}

    def _serialize(self, event):
        return {
            'id': event.id,
            'title': event.title,
            'event_type': event.event_type,
            'date': event.date.isoformat(),
            'notes': event.notes,
            'user_id': event.user_id,
            'bike_id': event.bike_id,
            'part_id': event.part_id,
            'ride_id': event.ride_id,
            'recurrence': event.recurrence,
            'timezone': event.timezone,
            'public': event.public
        }

