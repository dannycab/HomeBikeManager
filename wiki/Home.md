# HomeBikeManager Wiki

Welcome to the HomeBikeManager Wiki! This is a simplified, user-friendly version of the main documentation, focused on getting you started quickly.

## Quick Start

1. **Clone the repository**
   ```sh
   git clone https://github.com/dannycab/HomeBikeManager.git
   cd HomeBikeManager
   ```
2. **Set up a virtual environment and install dependencies**
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```
3. **Run the app**
   ```sh
   python app.py
   ```
4. **Or use Docker**
   ```sh
   docker build -t homebikemanager .
   docker run -p 5000:5000 homebikemanager
   ```

## What Can You Do?
- Register and log in users
- Manage bikes and parts (CRUD)
- See API documentation and usage examples

## What Isn't Ready Yet?
- Rides and file uploads (GPX/KML)
- Calendar/events
- Advanced authentication (JWT, OAuth)

For more details, see the [full documentation](https://dannycab.github.io/HomeBikeManager/) or the [GitHub README](../README.md).
