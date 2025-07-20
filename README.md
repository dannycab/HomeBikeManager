
# 🚲 HomeBikeManager

Welcome to HomeBikeManager! This is a humble, work-in-progress Flask REST API for managing your bikes, parts, rides, and maintenance schedules. It's not going to win any design awards, but it gets the job done (eventually). 😅

## Features (Such As They Are)
- 🛠️ Manage bikes and their parts (because you keep forgetting which chain fits which bike)
- 🗺️ Track rides, upload GPX/KML files (coming soon, we promise)
- 📅 Calendar for rides and maintenance (so you can ignore your own reminders)
- 🐳 Dockerized for easy deployment (or just run it locally, we won't judge)
- 🔑 API key authentication (security through obscurity?)
- 🧪 Automated tests (pytest, because we like green dots)
- 📝 Logging (so you can see all your mistakes in real time)

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

## Contributing
Pull requests welcome! Just don't expect us to merge them quickly. 😬

## License
MIT. Use at your own risk. Seriously.

---

*HomeBikeManager: Because your bikes deserve better, but this is what they get.*
