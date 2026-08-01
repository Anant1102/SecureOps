from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

from app.auth.auth_service import AuthService

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/api/auth"
)


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    response, status = AuthService.register_user(data)
    return jsonify(response), status


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    response, status = AuthService.login_user(data)
    return jsonify(response), status


@auth_bp.route("/profile", methods=["GET"])
@jwt_required()
def profile():

    current_user = get_jwt_identity()

    claims = get_jwt()

    return jsonify({
        "email": current_user,
        "role": claims["role"],
        "message": "Protected API Access Successful"
    }), 200