# Docker & Deployment

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
