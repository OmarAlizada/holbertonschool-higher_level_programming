#!/usr/bin/python3
"""Simple Flask API with users management and JSON endpoints."""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory dictionary to store users data
users = {}


@app.route("/", methods=["GET"])
def home():
    """Root endpoint returning greeting message."""
    return "Welcome to the Flask API!"


@app.route("/status", methods=["GET"])
def status():
    """Status endpoint returning OK status."""
    return "OK"


@app.route("/data", methods=["GET"])
def get_data():
    """Return a list of all usernames stored in the API."""
    return jsonify(list(users.keys()))


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Retrieve a specific user information by username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user via POST request with JSON payload."""
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400
        
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "User already exists"}), 400

    # Store user details in memory
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    response = {
        "message": "User added",
        "user": users[username]
    }
    return jsonify(response), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
