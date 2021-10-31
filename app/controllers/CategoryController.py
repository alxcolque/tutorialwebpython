from flask import render_template, url_for, request, redirect, flash
from app.models.Category import Category
from app import db
class CategoryController():
    def __init__(self):
        pass

    def index1(self):
        #users = User.query.all()
        return render_template('categories/index.html')
    def create(self):
        return render_template('categories/create.html')
    def store(self):
        if request.method == 'POST':
            category = request.form['category']
            categoryadd = Category(category = category)
            db.session.add(categoryadd)
            db.session.commit()
            flash('El registro se ha realizado con éxito.')
            return redirect(url_for('category_router.index'))
            
categorycontroller = CategoryController()