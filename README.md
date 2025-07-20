![HomeBikeManager Banner](docs/img/banner.png)

# 🚲 HomeBikeManager

[![Issues](https://img.shields.io/github/issues/dannycab/HomeBikeManager?style=flat-square)](https://github.com/dannycab/HomeBikeManager/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/dannycab/HomeBikeManager?style=flat-square)](https://github.com/dannycab/HomeBikeManager/pulls)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg?style=flat-square)](https://creativecommons.org/licenses/by-nc/4.0/)

> 📖 **Full documentation:** Visit the [Live Docs Website](https://dannycab.github.io/HomeBikeManager/) or see the [GitHub Wiki](https://github.com/dannycab/HomeBikeManager/wiki).

Welcome to HomeBikeManager! This is a humble, work-in-progress Flask REST API for managing your bikes, parts, rides, and maintenance schedules. It's not going to win any design awards, but it gets the job done (eventually). 😅

## System Overview
![HomeBikeManager Concept Diagram](docs/diagrams/homebikemanager_concept.svg)

*Figure 1: High-level concept diagram of the HomeBikeManager system, showing users, API, database, uploads, and main entities. This diagram provides a bird's-eye view of how the main components interact, including user actions, API endpoints, persistent storage, and the relationships between bikes, parts, rides, and calendar events.*

## Architecture & Workflows

### API Endpoints Map
![API Endpoints Map](docs/diagrams/api_endpoints_map.svg)

*Figure 2: This diagram shows the main REST API endpoints, their relationships, and how the API is organized. Each rectangle represents a resource (e.g., bikes, parts, rides), and arrows indicate management or interaction flows. Use this as a quick reference for endpoint structure and resource responsibilities.*

### Database Schema
![Database Schema](docs/diagrams/db_schema.svg)

*Figure 3: The database schema diagram illustrates the main models (User, Bike, Part, Ride, CalendarEvent) and their relationships. This helps developers understand how data is structured, how entities are linked, and how to extend the schema for new features.*

### Authentication Flow
![Authentication Flow](docs/diagrams/auth_flow.svg)

*Figure 4: This diagram details the authentication process, from user registration and login to API key issuance and request validation. It clarifies the security model and the steps required for secure access to the API.*

### File Upload Workflow
![File Upload Workflow](docs/diagrams/file_upload_flow.svg)

*Figure 5: This workflow shows how file uploads (GPX/KML) are validated, stored, and linked to rides. It covers validation, storage, and the connection between uploaded files and ride records.*

### Deployment Architecture
![Deployment Architecture](docs/diagrams/deployment_arch.svg)

*Figure 6: The deployment architecture diagram shows how the app, Docker container, database volume, uploads, and client interact. Use this to understand how to deploy, scale, and persist data in production.*

## Features (Such As They Are)

## Documentation Tree

All documentation is available on the [Live Docs Website](https://dannycab.github.io/HomeBikeManager/) (built with MkDocs Material) and is also suitable for the [Wiki](https://github.com/dannycab/HomeBikeManager/wiki).

```
docs/
  Home.md           # Wiki landing page
  setup.md          # Setup & Installation
  api.md            # API Reference
  uploads.md        # File Uploads
  auth.md           # Authentication
  docker.md         # Docker & Deployment
  testing.md        # Testing
  logging.md        # Logging & Debugging
  contributing.md   # Contributing
  faq.md            # FAQ
  scripts.md        # Automation Scripts
```

## Automation Scripts
See [docs/scripts.md](docs/scripts.md) for helper scripts, including `scripts/sync_docs_to_wiki.py` to copy docs/ to the wiki repo.

## Quick Start

1. Clone this repo (if you dare)
2. Install dependencies:
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # or .venv\\Scripts\\activate on Windows
   pip install -r requirements.txt
   ```
3. Run the app locally:
   ```sh
   python app.py
   ```
4. Or build and run with Docker:
   ```sh
   docker build -t homebikemanager .
   docker run -p 5000:5000 homebikemanager
   ```
5. Run the tests (if you trust them):
   ```sh
   pytest tests/
   ```

## API Endpoints
- `/api/register` – Register a new user (because you can't remember your old password)
- `/api/login` – Get an API key
- `/api/bikes` – CRUD for bikes
- `/api/parts` – CRUD for parts
- `/api/rides` – (coming soon)
- `/api/calendar` – (coming soon)

## What Works
- User registration & login
- API key authentication
- CRUD for bikes and parts
- Automated tests (pytest)
- Logging (so you can see what broke)

## What Doesn't (Yet)
- Rides and file uploads (GPX/KML)
- Calendar events
- Anything fancy

## Development Timeline
- **2025-07**: Project scaffolded, Flask app and models created, Docker and requirements set up.
- **2025-07**: User registration, login, and API key authentication implemented.
- **2025-07**: CRUD endpoints for bikes and parts added, with automated pytest-based tests.
- **2025-07**: Logging and error handling added.
- **2025-07**: .gitignore, documentation, and VS Code tasks improved.
- **2025-07**: GitHub issues filed for all major features and improvements.
- **2025-07**: docs/ folder created with actionable, status-aware documentation for all major features.
- **2025-07**: Automation script added to sync docs/ to the GitHub Wiki.

## Contributing
Pull requests welcome! Just don't expect us to merge them quickly. 😬

## License
Creative Commons Attribution-NonCommercial 4.0 International ([CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)).

See the [LICENSE](LICENSE) file for details.

---

*HomeBikeManager: Because your bikes deserve better, but this is what they get.*
