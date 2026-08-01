from flask_jwt_extended import create_access_token

from app.database.db import db
from app.models.user import User
from app.utils.password import hash_password, verify_password


class AuthService:

    @staticmethod
    def register_user(data):

        existing_user = User.query.filter_by(email=data["email"]).first()

        if existing_user:
            return {
                "success": False,
                "message": "Email already exists"
            }, 409

        user = User(
            employee_id=data["employee_id"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            password=hash_password(data["password"]),
            department=data["department"],
            team=data["team"],
            role=data["role"]
        )

        db.session.add(user)
        db.session.commit()

        return {
            "success": True,
            "message": "User registered successfully"
        }, 201

    @staticmethod
    def login_user(data):

        user = User.query.filter_by(email=data["email"]).first()

        if not user:
            return {
                "success": False,
                "message": "Invalid email or password"
            }, 401

        if not verify_password(data["password"], user.password):
            return {
                "success": False,
                "message": "Invalid email or password"
            }, 401

        access_token = create_access_token(
            identity=user.email,
            additional_claims={
                "role": user.role
            }
        )

        return {
            "success": True,
            "access_token": access_token
        }, 200