from app import db

team_projects = db.Table('team_projects', db.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('project_id', db.Integer, db.ForeignKey('projects.id'))
)

class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50))
    description = db.Column(db.String(250))
    status = db.Column(db.String(20))
    #relationship foreign
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    category = db.relationship("Category", back_populates="projects")
    user = db.relationship(
        "User",
        secondary=team_projects,
        back_populates="projects")
    task = db.relationship("Task", back_populates="projects")

