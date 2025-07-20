# Setup & Installation

## Prerequisites


## Project Status (July 2025)

| Feature                                 | Status      | Notes                                                      |
|-----------------------------------------|-------------|------------------------------------------------------------|
| Local setup (venv, requirements.txt)    | Built/Tested| Works as described                                         |
| Docker-based setup                      | Built/Tested| Dockerfile and deployment tested                           |
| Environment variable support            | Built       | .env.example provided; secrets/config expansion planned     |
| Docker volume for uploads/database      | Pending     | Recommended, not yet enforced                              |

**Summary:**
- Local and Docker-based setup are supported and tested.
- Environment variable usage is present but may need expansion for secrets/config.
- Docker volume for persistent uploads/database is recommended but not yet enforced.

## Local Setup
1. Clone the repository
2. Create a virtual environment and activate it
3. Install dependencies from requirements.txt
4. Set up environment variables (see .env.example)
5. Run the Flask app

## Docker Setup
1. Build the Docker image
2. Run the container with appropriate environment variables and volumes

See [docker.md](docker.md) for details.
# Setup & Installation

## Prerequisites

## Project Status
- Local and Docker-based setup are supported and tested.
- Environment variable usage is present but may need expansion for secrets/config.
- Docker volume for persistent uploads/database is recommended but not yet enforced.

## Local Setup
1. Clone the repository
2. Create a virtual environment and activate it
3. Install dependencies from requirements.txt
4. Set up environment variables (see .env.example)
5. Run the Flask app

## Docker Setup
1. Build the Docker image
2. Run the container with appropriate environment variables and volumes

See [docker.md](docker.md) for details.
