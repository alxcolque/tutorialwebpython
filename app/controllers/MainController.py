from flask import render_template
class MainController():
    def __init__(self):
        pass

    def index(self):
        user1 = {'name': 'Tupaj','surname':'Martinez'}
        return render_template('index.html', user=user1)
maincontroller = MainController()