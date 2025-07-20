# Authentication

HomeBikeManager uses username/password authentication and API keys.

## Project Status
- User registration and login endpoints are implemented and tested.
- API key authentication is implemented and tested.
- Advanced authentication (JWT/OAuth2, rate limiting) is planned.

## Registration & Login
- POST /register
- POST /login

## API Key Usage
- Pass API key in Authorization header

## Security Best Practices
- Never share your API key
- Use HTTPS in production
