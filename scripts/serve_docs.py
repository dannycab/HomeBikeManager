#!/usr/bin/env python3
"""
serve_docs.py - Simple static server for docs/ folder

Usage:
  python scripts/serve_docs.py [--port 8000]

Serves the docs/ directory at http://localhost:8000 (default port).
"""
import http.server
import socketserver
import os
import sys

PORT = 8000
if len(sys.argv) > 1 and sys.argv[1].startswith('--port'):
    try:
        PORT = int(sys.argv[1].split('=')[1])
    except Exception:
        pass

DOCS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'docs')
os.chdir(DOCS_DIR)

Handler = http.server.SimpleHTTPRequestHandler

print(f"Serving docs/ at http://localhost:{PORT} (Ctrl+C to stop)")
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
