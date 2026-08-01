from flask import Blueprint, jsonify

employee_bp = Blueprint("employee", __name__)

@employee_bp.get("/api/employees")
def list_employees():
    return jsonify([])
