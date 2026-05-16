#!/usr/bin/python3
"""Simple API using http.server with JSON endpoints."""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPI(BaseHTTPRequestHandler):
    """Handles HTTP requests for a simple API."""

    def do_GET(self):
        """Handle GET requests and route endpoints."""
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"status": "OK"}
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"error": "Resource not found"}
            self.wfile.write(json.dumps(data).encode("utf-8"))


if __name__ == "__main__":
    server = HTTPServer(("", 8000), SimpleAPI)
    print("Server running on port 8000...")
    server.serve_forever()
