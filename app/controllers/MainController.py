from flask import render_template
class MainController():
    def __init__(self):
        pass

    def index(self):
        #user = {'name': 'Tupaj Katali'}
        return render_template('index.html')
maincontroller = MainController()