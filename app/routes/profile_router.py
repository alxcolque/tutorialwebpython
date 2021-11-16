from flask import Blueprint
from app.controllers.ProfileController import profilecontroller
from flask_login import login_required

profile_router = Blueprint('profile_router', __name__)

@login_required
@profile_router.route('/profile',methods=['GET'])
def index():
    return profilecontroller.index()

@login_required
@profile_router.route('/updateprofile',methods=['POST'])
def updateprofile():
    return profilecontroller.updateprofile()
