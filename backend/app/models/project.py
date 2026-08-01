from datetime import datetime

from app.database.db import db


class Project(db.Model):

    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(
        db.String(150),
        nullable=False,
        unique=True
    )

    description = db.Column(
        db.Text,
        nullable=False
    )

    repository = db.Column(
        db.String(255),
        nullable=False
    )

    language = db.Column(
        db.String(50),
        nullable=False
    )

    environment = db.Column(
        db.String(50),
        nullable=False
    )

    owner = db.Column(
        db.String(150),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):
        return f"<Project {self.name}>"