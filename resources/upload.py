import logging
from flask import request, jsonify
from flask_restful import Resource
import os
from werkzeug.utils import secure_filename

logger = logging.getLogger(__name__)

UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', 'uploads')
ALLOWED_EXTENSIONS = {'gpx', 'kml'}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

class FileUploadResource(Resource):
    def post(self):
        if 'file' not in request.files:
            logger.warning('No file part in request')
            return {'error': 'No file part'}, 400
        file = request.files['file']
        if file.filename == '':
            logger.warning('No selected file')
            return {'error': 'No selected file'}, 400
        if not self.allowed_file(file.filename):
            logger.warning('Invalid file type')
            return {'error': 'Invalid file type'}, 400
        if len(file.read()) > MAX_FILE_SIZE:
            logger.warning('File too large')
            return {'error': 'File too large'}, 400
        file.seek(0)
        filename = secure_filename(file.filename)
        save_path = os.path.join(UPLOAD_FOLDER, filename)
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        file.save(save_path)
        logger.info(f'File uploaded: {filename}')
        return {'message': 'File uploaded', 'filename': filename}, 201

    @staticmethod
    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
