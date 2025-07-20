# API Reference

This section documents the main REST API endpoints for HomeBikeManager.

## Project Status
- Auth endpoints (register, login) are implemented and tested.
- Bike and part endpoints are implemented and tested.
- Rides and calendar/event endpoints are not yet implemented (models exist).
- Error handling and logging are present but should be reviewed for all endpoints.

## Authentication
- POST /register
- POST /login
- API key usage

## Bikes
- GET /bikes
- POST /bikes
- GET /bikes/<id>
- PUT /bikes/<id>
- DELETE /bikes/<id>

## Parts
- GET /parts
- POST /parts
- ...

## Rides
- Endpoints for rides and file uploads (see [uploads.md](uploads.md))

## Calendar/Events
- Endpoints for calendar and event management

### Example Request
```bash
curl -X GET "http://localhost:5000/bikes" -H "Authorization: Bearer <API_KEY>"
```

### Error Responses
- Standardized error format
- HTTP status codes
