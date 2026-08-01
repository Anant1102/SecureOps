from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from app.services.project_service import ProjectService

project_bp = Blueprint(
    "projects",
    __name__,
    url_prefix="/api/projects"
)


@project_bp.route("", methods=["POST"])
@jwt_required()
def create_project():

    data = request.get_json()

    response, status = ProjectService.create_project(data)

    return jsonify(response), status


@project_bp.route("", methods=["GET"])
@jwt_required()
def get_projects():

    response, status = ProjectService.get_projects()

    return jsonify(response), status