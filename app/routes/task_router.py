from flask import Blueprint
from app.controllers.TaskController import taskcontroller
from flask_login import login_required

task_router = Blueprint('task_router', __name__)

@task_router.route('/tasks',methods=['GET'])
@login_required
def index():
    return taskcontroller.index()
@task_router.route('/tasks1',methods=['GET'])
@login_required
def index1():
    return taskcontroller.index1()

@task_router.route('/tasks/store',methods=['POST'])
@login_required
def store():
    return taskcontroller.store()

@task_router.route('/tasks/<int:id>/delete',methods=['GET'])
@login_required
def delete(id):
    return taskcontroller.delete(id)

@task_router.route('/tasks/<int:id>/edit',methods=['GET'])
@login_required
def edit(id):
    return taskcontroller.edit(id)

@task_router.route('/tasks/<int:id>/update',methods=['POST'])
@login_required
def update(id):
    return taskcontroller.update(id)

#print
@task_router.route('/convertpdf',methods=['GET'])
@login_required
def convertpdf():
    return taskcontroller.convertpdf()
