from flask import render_template, url_for
class CategoryController():
    def __init__(self):
        pass

    def index1(self):
        #users = User.query.all()
        return render_template('categories/index.html')
    def create(self):
        return render_template('categories/create.html')
categorycontroller = CategoryController()