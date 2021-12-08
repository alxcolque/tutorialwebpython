from flask import Blueprint
from app.controllers.ProfileController import profilecontroller
from flask_login import login_required

profile_router = Blueprint('profile_router', __name__)


@profile_router.route('/profile',methods=['GET'])
@login_required
def index():
    return profilecontroller.index()

@profile_router.route('/updateprofile',methods=['POST'])
@login_required
def updateprofile():
    return profilecontroller.updateprofile()
