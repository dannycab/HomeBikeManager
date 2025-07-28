# syntax=docker/dockerfile:1
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


# Create persistent upload directory for volume mount
RUN mkdir -p /data/uploads && chmod 777 /data/uploads

COPY . .

EXPOSE 5000
CMD ["python", "app.py"]
