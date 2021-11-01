from flask import render_template, url_for, request, redirect, flash
from app.models.Category import Category
from app import db
class CategoryController():
    def __init__(self):
        pass

    def index1(self):
        categories = Category.query.all()
        return render_template('categories/index.html',categories=categories)
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
    def delete(self, _id):
        category = Category.query.get(_id)
        db.session.delete(category)
        db.session.commit()
        flash('El registro se ha eliminado con éxito.')
        return redirect(url_for('category_router.index'))
    def edit(self, _id):
        category = Category.query.get(_id)
        return render_template('categories/edit.html',category=category)
    def update(self, _id):
        if request.method == 'POST':
            categoryV = request.form['category']
            categoryDB = Category.query.get(_id)
            categoryDB.category = categoryV
            db.session.commit()
            flash('El registro se ha actualizado con éxito.')
            return redirect(url_for('category_router.index'))
            
categorycontroller = CategoryController()