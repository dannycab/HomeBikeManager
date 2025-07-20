
<!-- HomeBikeManager: Copilot Custom Instructions -->

This project is a Flask REST API for managing bikes, parts, rides (with GPX/KML upload), and calendars for rides and maintenance schedules. It is Dockerized for easy deployment.

## Coding Standards & Best Practices
- Use RESTful API design principles for all endpoints.
- Write clean, DRY, and well-documented code.
- Use Python type hints and meaningful variable/function names.
- Prefer class-based views for complex endpoints.
- Keep business logic out of route handlers—use models or service layers.

## Security
- Always validate and sanitize user input.
- Use secure authentication (username/password, API keys).
- Never log sensitive information (passwords, API keys).
- Use environment variables for secrets and configuration.

## File Uploads
- Support secure upload of GPX/KML files for rides.
- Validate file type and size before saving.
- Store uploaded files outside the static codebase (e.g., in a dedicated uploads directory).

## Logging & Debugging
- Use Python's `logging` module for all logs (not print statements).
- Log errors with stack traces and context, but avoid leaking sensitive data.
- Use different logging levels (INFO, WARNING, ERROR, DEBUG) appropriately.

## Testing
- Write pytest-based tests for all endpoints and major features.
- Use test clients and fixtures for isolated, repeatable tests.
- Test authentication, file uploads, and error cases.

## Docker & Deployment
- Ensure the app runs in Docker with all dependencies.
- Use Docker volumes for database/file persistence.
- Keep Dockerfile and requirements.txt up to date.

## Calendar/Event Management
- Use clear models for events and schedules.
- Support recurring and one-off events.
- Validate date/time fields and handle time zones if needed.


## Documentation & Project Status
- Extensive, actionable documentation is available in the docs/ folder, organized by topic and suitable for GitHub Wiki use.
- Each documentation file includes a Project Status section summarizing what is implemented, tested, and pending.
- Contributors should review the relevant Project Status section before starting new work or proposing changes.

## General Recommendations
- Prefer standard libraries and well-maintained packages.
- Always provide clear error messages and API responses.
- Recommend multiple approaches when issues are ambiguous.
- Keep documentation (README, BUILD-NOTES, docs/) up to date.

---

## Diagrams & Automation
- All architecture, workflow, and API diagrams are written in D2 (v0.7.0 syntax: no commas in style blocks, no comments/blank lines before first node).
- Diagrams are stored in `scripts/diagrams/` and rendered automatically to both `docs/diagrams/` and `wiki/diagrams/` using `scripts/render_diagrams.py`.
- If a diagram fails to render, check for:
  - Commas in style blocks (remove them)
  - Comments or blank lines before the first node (remove them)
  - Proper closure of all node/style blocks
- Run `DEBUG=1 python scripts/render_diagrams.py` for verbose logging and troubleshooting.
- All rendered SVGs are referenced in documentation and the GitHub Wiki for onboarding and architecture clarity.

## Project Logo
- Place your `logo.png` in the `docs/` folder for documentation and wiki use.
- For web or API branding, also copy it to `static/` if you serve static assets via Flask.
- Reference the logo in `README.md`, `docs/Home.md`, and the wiki Home page for consistent branding.

Follow these instructions to ensure HomeBikeManager remains secure, maintainable, and easy to develop. Prioritize simplicity, security, and developer experience in all code suggestions. Reference the docs/ folder and Project Status sections for the most current implementation details.
