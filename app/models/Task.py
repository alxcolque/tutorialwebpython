from app import db
class SubTask(db.Model):
    __tablename__ = 'sub_tasks'
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'), primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), primary_key=True)
    description = db.Column(db.String(250))
    status_progress = db.Column(db.String(20))
    #task = db.relationship("Task", back_populates="projects")
    #project = db.relationship("Project", back_populates="tasks")

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task = db.Column(db.String(50))
    date_begin = db.Column(db.Date)
    date_end = db.Column(db.Date)
    #project = db.relationship("Project", back_populates="tasks")