from app.models.User import User
from app import db
from flask import render_template
class MainController():
    def __init__(self):
        pass

    def index(self):
        return render_template('home.html')
maincontroller = MainController()