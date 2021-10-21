from app.models.User import User
from app.models.Task import Task
from app.models.Category import Category
from app.models.Project import Project

from app import db

db.drop_all()
db.create_all()