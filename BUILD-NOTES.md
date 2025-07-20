# BUILD-NOTES.md

## Project: HomeBikeManager

### Timeline & Major Steps

**2025-07-20**
- Project initialized as a Flask REST API for managing bikes, parts, rides, and calendar events.
- Dockerfile, requirements.txt, and VS Code tasks created for easy development and deployment.
- Initial app scaffolded with `/` root endpoint.

**API & Models**
- Models for User, Bike, Part, Ride, and CalendarEvent created using SQLAlchemy.
- RESTful endpoints for bikes and parts implemented with Flask-RESTful.
- User registration and login endpoints added, with API key authentication for all other endpoints.
- Passwords stored securely using Werkzeug hashing.

**Testing & Development**
- Automated test script created using pytest and requests, covering registration, login, bike, and part endpoints.
- Logging added to the Flask app for all major actions and errors.
- Date parsing for `purchase_date` and `install_date` fixed for both create and update endpoints.
- Tests run and passed locally using a Python virtual environment, with persistent SQLite database.

**Project Hygiene**
- .gitignore filled out for Python, macOS, Windows, and Linux development.
- All development artifacts, OS files, and virtual environments excluded from version control.


**2025-07-20 (cont.)**
- Added `scripts/sync_docs_to_wiki.py` to automate copying Markdown docs to the Wiki and running `git add .`, `git commit`, and `git push` for seamless documentation updates.
- Removed custom CSS from MkDocs configuration to resolve build and compatibility issues with the Material theme.

**Known Gaps / Next Steps**
- Rides, file upload, and calendar endpoints to be implemented.
- Docker volume for database persistence (optional for production).
- More advanced authentication (JWT, OAuth) and user management if needed.
- Additional tests for rides, calendar, and file upload.

---

This file logs the major steps, fixes, and decisions made during the build of HomeBikeManager. Update as the project evolves!
