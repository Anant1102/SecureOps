from app.database.db import db
from app.models.project import Project


class ProjectService:

    @staticmethod
    def create_project(data):

        project = Project(
            name=data["name"],
            description=data["description"],
            repository=data["repository"],
            language=data["language"],
            environment=data["environment"],
            owner=data["owner"]
        )

        db.session.add(project)
        db.session.commit()

        return {
            "success": True,
            "message": "Project created successfully"
        }, 201

    @staticmethod
    def get_projects():

        projects = Project.query.all()

        result = []

        for project in projects:
            result.append({
                "id": project.id,
                "name": project.name,
                "repository": project.repository,
                "environment": project.environment,
                "language": project.language,
                "owner": project.owner
            })

        return result, 200