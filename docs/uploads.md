# File Uploads

HomeBikeManager supports secure upload of GPX and KML files for rides.

## Project Status
- File upload endpoints and logic are not yet implemented.
- Models support file path storage for rides.
- Secure file validation and storage are planned.

## Upload Guidelines
- Only GPX and KML files are accepted
- File size limits enforced
- Files stored outside the static codebase

## Example
```bash
curl -X POST -F "file=@ride.gpx" http://localhost:5000/rides/upload -H "Authorization: Bearer <API_KEY>"
```
