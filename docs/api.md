# This file does not contain any <link> or <nav> elements to remove.
# API Reference

This section documents the main REST API endpoints for HomeBikeManager.


## Project Status (July 2025)

| Feature                        | Status      | Notes                                             |
|--------------------------------|-------------|---------------------------------------------------|
| Auth endpoints (register/login)| Built/Tested| Implemented and tested                            |
| Bike and part endpoints        | Built/Tested| Implemented and tested                            |
| Rides endpoints                | Pending     | Models exist, endpoints not yet implemented       |
| Calendar/event endpoints       | Pending     | Models exist, endpoints not yet implemented       |
| Error handling/logging         | Built       | Present, should be reviewed for all endpoints     |

**Summary:**
- Auth, bike, and part endpoints are implemented and tested.
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

## API Endpoints Map
![API Endpoints Map](diagrams/api_endpoints_map.svg)

*Figure: This diagram shows the main REST API endpoints, their relationships, and how the API is organized. Each rectangle represents a resource (e.g., bikes, parts, rides), and arrows indicate management or interaction flows. Use this as a quick reference for endpoint structure and resource responsibilities.*

## Database Schema
![Database Schema](diagrams/db_schema.svg)

*Figure: The database schema diagram illustrates the main models (User, Bike, Part, Ride, CalendarEvent) and their relationships. This helps developers understand how data is structured, how entities are linked, and how to extend the schema for new features.*

### Example Request
```bash
curl -X GET "http://localhost:5000/bikes" -H "Authorization: Bearer <API_KEY>"
```

### Error Responses
- Standardized error format
- HTTP status codes
