
# 🚲 HomeBikeManager

Welcome to HomeBikeManager! This is a humble, work-in-progress Flask REST API for managing your bikes, parts, rides, and maintenance schedules. It's not going to win any design awards, but it gets the job done (eventually). 😅

## System Overview
![HomeBikeManager Concept Diagram](docs/diagrams/homebikemanager_concept.svg)

*Figure: High-level concept diagram of the HomeBikeManager system, showing users, API, database, uploads, and main entities.*

## Features (Such As They Are)

## Documentation Tree
All documentation is in the `docs/` folder and is suitable for the GitHub Wiki. See also the [Wiki](https://github.com/dannycab/HomeBikeManager/wiki).

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
MIT. Use at your own risk. Seriously.

---

*HomeBikeManager: Because your bikes deserve better, but this is what they get.*
