from flask import Blueprint

employee_bp = Blueprint("employee", __name__)

@employee_bp.get("/employees")
def get_employees():
    return []
