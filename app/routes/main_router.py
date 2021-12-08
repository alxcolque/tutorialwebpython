from flask import Blueprint
from app.controllers.MainController import maincontroller
from flask_login import login_required

main_router = Blueprint('main_router', __name__)

@main_router.route('/home',methods=['GET'])
@login_required
def main():
    return maincontroller.index()
