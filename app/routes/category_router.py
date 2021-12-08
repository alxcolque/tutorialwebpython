from flask import Blueprint
from app.controllers.CategoryController import categorycontroller
from flask_login import login_required

category_router = Blueprint('category_router', __name__)

@category_router.route('/categories',methods=['GET'])
@login_required
def index():
    return categorycontroller.index1()

@category_router.route('/categories/create',methods=['GET'])
@login_required
def create():
    return categorycontroller.create()

@category_router.route('/categories/store',methods=['POST'])
@login_required
def store():
    return categorycontroller.store()

@category_router.route('/categories/<int:id>/delete',methods=['GET'])
@login_required
def delete(id):
    return categorycontroller.delete(id)

@category_router.route('/categories/<int:id>/edit',methods=['GET'])
@login_required
def edit(id):
    return categorycontroller.edit(id)

@category_router.route('/categories/<int:id>/update',methods=['POST'])
@login_required
def update(id):
    return categorycontroller.update(id)