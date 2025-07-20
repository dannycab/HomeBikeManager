# Authentication

HomeBikeManager uses username/password authentication and API keys.

## Authentication Flow
![Authentication Flow](diagrams/auth_flow.svg)

*Figure: This diagram details the authentication process, from user registration and login to API key issuance and request validation. It clarifies the security model and the steps required for secure access to the API.*


## Project Status (July 2025)

| Feature                        | Status      | Notes                                             |
|--------------------------------|-------------|---------------------------------------------------|
| User registration/login        | Built/Tested| Implemented and tested                            |
| API key authentication         | Built/Tested| Implemented and tested                            |
| Advanced authentication        | Planned     | JWT/OAuth2, rate limiting planned                 |

**Summary:**
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
