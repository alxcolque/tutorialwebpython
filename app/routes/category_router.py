from flask import Blueprint
from app.controllers.CategoryController import categorycontroller

category_router = Blueprint('category_router', __name__)

@category_router.route('/categories',methods=['GET'])
def index():
    return categorycontroller.index1()

@category_router.route('/categories/create',methods=['GET'])
def create():
    return categorycontroller.create()

@category_router.route('/categories/store',methods=['POST'])
def store():
    return categorycontroller.store()