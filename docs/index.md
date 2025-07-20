
<link rel="stylesheet" href="style.css">
<nav>
  <a href="index.md" class="active">Home</a>
  <a href="setup.md">Setup</a>
  <a href="api.md">API</a>
  <a href="uploads.md">Uploads</a>
  <a href="auth.md">Auth</a>
  <a href="docker.md">Docker</a>
  <a href="testing.md">Testing</a>
  <a href="logging.md">Logging</a>
  <a href="contributing.md">Contributing</a>
  <a href="faq.md">FAQ</a>
</nav>

![HomeBikeManager Banner](img/banner.png)

## Contents
- [Setup & Installation](setup.md)
- [API Reference](api.md)
- [File Uploads](uploads.md)
- [Authentication](auth.md)
- [Docker & Deployment](docker.md)
- [Testing](testing.md)
- [Logging & Debugging](logging.md)
- [Contributing](contributing.md)
- [FAQ](faq.md)

# HomeBikeManager Documentation

Welcome to the HomeBikeManager documentation. This guide covers everything you need to develop, deploy, and use the HomeBikeManager Flask REST API.

## System Overview
<img src="diagrams/homebikemanager_concept.svg" alt="HomeBikeManager Concept Diagram" width="50%" />

*Figure 1: High-level concept diagram of the HomeBikeManager system, showing users, API, database, uploads, and main entities. This diagram provides a bird's-eye view of how the main components interact, including user actions, API endpoints, persistent storage, and the relationships between bikes, parts, rides, and calendar events.*

## Architecture & Workflows

### API Endpoints Map
<img src="diagrams/api_endpoints_map.svg" alt="API Endpoints Map" width="50%" />

*Figure 2: This diagram shows the main REST API endpoints, their relationships, and how the API is organized. Each rectangle represents a resource (e.g., bikes, parts, rides), and arrows indicate management or interaction flows. Use this as a quick reference for endpoint structure and resource responsibilities.*

### Database Schema
<img src="diagrams/db_schema.svg" alt="Database Schema" width="50%" />

*Figure 3: The database schema diagram illustrates the main models (User, Bike, Part, Ride, CalendarEvent) and their relationships. This helps developers understand how data is structured, how entities are linked, and how to extend the schema for new features.*

### Authentication Flow
<img src="diagrams/auth_flow.svg" alt="Authentication Flow" width="50%" />

*Figure 4: This diagram details the authentication process, from user registration and login to API key issuance and request validation. It clarifies the security model and the steps required for secure access to the API.*

### File Upload Workflow
<img src="diagrams/file_upload_flow.svg" alt="File Upload Workflow" width="50%" />

*Figure 5: This workflow shows how file uploads (GPX/KML) are validated, stored, and linked to rides. It covers validation, storage, and the connection between uploaded files and ride records.*

### Deployment Architecture
<img src="diagrams/deployment_arch.svg" alt="Deployment Architecture" width="50%" />

*Figure 6: The deployment architecture diagram shows how the app, Docker container, database volume, uploads, and client interact. Use this to understand how to deploy, scale, and persist data in production.*

## Project Status (as of July 2025)
- User registration, login, and API key authentication are implemented and tested.
- Bike and part endpoints are implemented and tested.
- Models for rides and calendar events exist, but endpoints and file upload logic are not yet implemented.
- Dockerfile and requirements.txt are present and functional.
- Pytest-based tests cover authentication, bikes, and parts.
- Logging is set up using Python’s logging module.
- File upload, advanced authentication, and calendar/ride endpoints are pending.

## Contents
- [Setup & Installation](setup.md)
- [API Reference](api.md)
- [File Uploads](uploads.md)
- [Authentication](auth.md)
- [Docker & Deployment](docker.md)
- [Testing](testing.md)
- [Logging & Debugging](logging.md)
- [Contributing](contributing.md)
- [FAQ](faq.md)
