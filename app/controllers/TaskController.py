from flask import render_template, url_for, request, redirect, flash, make_response
from app.models.Task import Task
from app import db, app
import pdfkit
import os
app.config['PDF_FOLDER'] = 'app/static/pdf/'
app.config['TEMPLATE_FOLDER'] = 'app/views/tasks/'
URL_INDEX_TO_PRINT = 'http://127.0.0.1:5001/tasks'
WKHTMLTOPDF_PATH = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
class TaskController():
    def __init__(self):
        pass

    def index(self):
        tasks = Task.query.all()
        return render_template('tasks/index.html', tasks=tasks)
    def index1(self):
        tasks = Task.query.all()
        return render_template('tasks/index1.html', tasks=tasks)

    def store(self):
        if request.method == 'POST':
            task = request.form['task']
            date_begin = request.form['date_begin']
            date_end = request.form['date_end']

            taskadd = Task(task=task, date_begin=date_begin, date_end=date_end)
            db.session.add(taskadd)
            db.session.commit()
            # flash('El registro se ha realizado con éxito.')
            return redirect(url_for('task_router.index'))

    def delete(self, _id):
        task = Task.query.get(_id)
        db.session.delete(task)
        db.session.commit()
        flash('El registro se ha eliminado con éxito.')
        return redirect(url_for('task_router.index'))

    def edit(self, _id):
        category = Task.query.get(_id)
        return render_template('categories/edit.html', category=category)

    def update(self, _id):
        if request.method == 'POST':
            categoryV = request.form['category']
            categoryDB = Task.query.get(_id)
            categoryDB.category = categoryV
            db.session.commit()
            flash('El registro se ha actualizado con éxito.')
            return redirect(url_for('category_router.index'))
            
    def convertpdf(self):
        config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)
        #htmlfile = app.config['TEMPLATE_FOLDER'] + 'index.html'
        htmlfile = 'http://127.0.0.1:5001/tasks'
        #img = ''
        tasks = Task.query.all()
        header = '''
        
        
        '''
        body = render_template('tasks/index1.html', tasks=tasks)
        footer= '''<p>Fin de todo</p>'''
        #htmlfile = header+body+footer
        #htmlfile = "<img src='https://conceptodefinicion.de/wp-content/uploads/2014/05/Imagen-2.jpg'>"
        
        pdffile = app.config['PDF_FOLDER'] + 'demo.pdf'
        options={
                'page-size': 'Letter',
                'margin-top': '0.75in',
                'margin-right': '0.75in',
                'margin-bottom': '0.75in',
                'margin-left': '0.75in',
                'encoding': "UTF-8",
                'custom-header': [
                    ('Accept-Encoding', 'gzip')
                ],
            }
        css = 'app/static/css/style.css'
        try:
            pdfkit.from_url(htmlfile, pdffile, configuration=config, options=options)
            #pdfkit.from_file(htmlfile, pdffile,configuration=config, options=options)
            
            #pdfkit.from_string(htmlfile, pdffile,configuration=config, options=options)
            return '''Click here to open the <a href="http://127.0.0.1:5001/static/pdf/demo.pdf">pdf</a>.'''
        except OSError as e:
            if 'Done' not in str(e):
                raise e
        


taskcontroller = TaskController()
