from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Allow frontend to communicate with backend
CORS(app)


# =========================
# User Model
# =========================

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )


# =========================
# Create Database
# =========================

with app.app_context():
    db.create_all()


# =========================
# Register API
# =========================

@app.route("/api/auth/register", methods=["POST"])
def register():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    # Validation
    if not username or not password:

        return jsonify({
            "success": False,
            "message": "Username and password are required"
        }), 400


    # Check username
    user = User.query.filter_by(
        username=username
    ).first()

    if user:

        return jsonify({
            "success": False,
            "message": "Username already exists"
        }), 409


    # Hash password
    password_hash = generate_password_hash(password)


    # Create user
    new_user = User(
        username=username,
        password=password_hash
    )

    db.session.add(new_user)
    db.session.commit()


    return jsonify({
        "success": True,
        "message": "Registration successful"
    }), 201


# =========================
# Login API
# =========================

@app.route("/api/auth/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")


    if not username or not password:

        return jsonify({
            "success": False,
            "message": "Username and password are required"
        }), 400


    # Find user
    user = User.query.filter_by(
        username=username
    ).first()


    if not user:

        return jsonify({
            "success": False,
            "message": "Invalid username or password"
        }), 401


    # Check password
    if not check_password_hash(
        user.password,
        password
    ):

        return jsonify({
            "success": False,
            "message": "Invalid username or password"
        }), 401


    return jsonify({
        "success": True,
        "message": "Login successful",

        "user": {
            "id": user.id,
            "username": user.username
        }
    }), 200


# =========================
# Run
# =========================

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )