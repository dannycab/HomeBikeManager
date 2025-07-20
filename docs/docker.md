# Docker & Deployment
## Deployment Architecture
![Deployment Architecture](diagrams/deployment_arch.svg)
*Figure: The deployment architecture diagram shows how the app, Docker container, database volume, uploads, and client interact. Use this to understand how to deploy, scale, and persist data in production.*
## Running with Docker
## Project Status
- Dockerfile and requirements.txt are present and functional.
- Docker-based deployment is supported.
- Docker volume for persistent uploads/database is recommended but not yet enforced.
## Example Commands
```bash
docker build -t homebikemanager .
docker run -d -p 5000:5000 --env-file .env -v $(pwd)/uploads:/app/uploads homebikemanager
```
# Docker & Deployment

## Deployment Architecture
![Deployment Architecture](diagrams/deployment_arch.svg)

*Figure: The deployment architecture diagram shows how the app, Docker container, database volume, uploads, and client interact. Use this to understand how to deploy, scale, and persist data in production.*

## Running with Docker

## Project Status
- Dockerfile and requirements.txt are present and functional.
- Docker-based deployment is supported.
- Docker volume for persistent uploads/database is recommended but not yet enforced.

## Example Commands
```bash
docker build -t homebikemanager .
docker run -d -p 5000:5000 --env-file .env -v $(pwd)/uploads:/app/uploads homebikemanager
```
