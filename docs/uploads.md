# File Uploads

HomeBikeManager supports secure upload of GPX and KML files for rides.


## Project Status (July 2025)

| Feature                        | Status      | Notes                                             |
|--------------------------------|-------------|---------------------------------------------------|
| File upload endpoints          | Pending     | Not yet implemented                               |
| Ride model file path support   | Built       | Models support file path storage for rides         |
| Secure file validation/storage | Pending     | Planned                                           |

**Summary:**
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

## File Upload Workflow
![File Upload Workflow](diagrams/file_upload_flow.svg)

*Figure: This workflow shows how file uploads (GPX/KML) are validated, stored, and linked to rides. It covers validation, storage, and the connection between uploaded files and ride records.*
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

## File Upload Workflow
![File Upload Workflow](diagrams/file_upload_flow.svg)

*Figure: This workflow shows how file uploads (GPX/KML) are validated, stored, and linked to rides. It covers validation, storage, and the connection between uploaded files and ride records.*
