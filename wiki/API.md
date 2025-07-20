# API Quick Reference

## Main Endpoints
- `/api/register` – Register a new user
- `/api/login` – Get an API key
- `/api/bikes` – CRUD for bikes
- `/api/parts` – CRUD for parts
- `/api/rides` – (coming soon)
- `/api/calendar` – (coming soon)

## Authentication
- Register and login endpoints are available
- API key required for all other endpoints (pass in `Authorization` header)

## Example Request
```bash
curl -X GET "http://localhost:5000/api/bikes" -H "Authorization: Bearer <API_KEY>"
```

For more details and error formats, see the [full API docs](https://dannycab.github.io/HomeBikeManager/api/).
