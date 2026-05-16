#!/usr/bin/python3
"""API Security and Authentication Techniques using Flask."""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# JWT Configuration
app.config["JWT_SECRET_KEY"] = "super-secret-key-change-me"
jwt = JWTManager(app)
auth = HTTPBasicAuth()

# In-memory users data with role-based structure
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """Verify the provided username and password for Basic Auth."""
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


@app.route("/login", methods=["POST"])
def login():
    """Generate a JWT token upon successful credentials check."""
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Missing JSON in request"}), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        # Include username and role in the JWT identity payload
        identity = {"username": username, "role": user["role"]}
        access_token = create_access_token(identity=identity)
        return jsonify(access_token=access_token), 200

    return jsonify({"error": "Invalid credentials"}), 401


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """Protected route via Basic Authentication."""
    return "Basic Auth: Access Granted", 200


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """Protected route via JWT Token Authentication."""
    return "JWT Auth: Access Granted", 200


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """Admin-only endpoint checking identity attributes inside token."""
    current_user = get_jwt_identity()
    if current_user.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted", 200


# Custom Error Handlers for handling JWT authentication edge cases
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
