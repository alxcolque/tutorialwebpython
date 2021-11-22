from flask import render_template, url_for, request, redirect, flash
from app.models.Project import Project
from app.models.Task import Task, SubTask
from app import db
class TaskController():
    def __init__(self):
        pass

    def index(self):
        tasks = Task.query.all()#Practica.query.join(Materia).filter().all()
        return render_template('tasks/index.html',tasks=tasks)
    def create(self):
        return render_template('categories/create.html')
    def store(self):
        if request.method == 'POST':
            category = request.form['category']
            categoryadd = Task(category = category)
            db.session.add(categoryadd)
            db.session.commit()
            flash('El registro se ha realizado con éxito.')
            return redirect(url_for('category_router.index'))
    def delete(self, _id):
        category = Task.query.get(_id)
        db.session.delete(category)
        db.session.commit()
        flash('El registro se ha eliminado con éxito.')
        return redirect(url_for('category_router.index'))
    def edit(self, _id):
        category = Task.query.get(_id)
        return render_template('categories/edit.html',category=category)
    def update(self, _id):
        if request.method == 'POST':
            categoryV = request.form['category']
            categoryDB = Task.query.get(_id)
            categoryDB.category = categoryV
            db.session.commit()
            flash('El registro se ha actualizado con éxito.')
            return redirect(url_for('category_router.index'))
            
taskcontroller = TaskController()