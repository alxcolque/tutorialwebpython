from flask import Blueprint
from app.controllers.TaskController import taskcontroller

task_router = Blueprint('task_router', __name__)

@task_router.route('/tasks',methods=['GET'])
def index():
    return taskcontroller.index1()

@task_router.route('/tasks/store',methods=['POST'])
def store():
    return taskcontroller.store()

@task_router.route('/tasks/<int:id>/delete',methods=['GET'])
def delete(id):
    return taskcontroller.delete(id)

@task_router.route('/tasks/<int:id>/edit',methods=['GET'])
def edit(id):
    return taskcontroller.edit(id)

@task_router.route('/tasks/<int:id>/update',methods=['POST'])
def update(id):
    return taskcontroller.update(id)