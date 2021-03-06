from flask import render_template, url_for, request, redirect, flash
from app.models.User import User
from app import db, app
from flask_login import current_user

import os
import time
from PIL import Image #pip install pillow
import urllib.request
from werkzeug.utils import secure_filename


class ProfileController():
    def __init__(self):
        pass

    def index(self):
        iduser = current_user.id
        user = User.query.get(iduser)
        return render_template('profile/index.html', user=user)
    def updateprofile(self):
        if request.method == 'POST':
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            if file.filename == '':
                flash('No image selected for uploading')
                return redirect(request.url)
            if file: #and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                #guardar nombre
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                
                fecha = time.strftime("%Y%m%d%H%M%S")
                imgPath = app.config['UPLOAD_FOLDER'] + filename
                img = Image.open(imgPath)
                img.save('app/static/uploads/'+fecha+'.png')
                os.remove('app/static/uploads/'+filename)
                newfilename = fecha+'.png'

                iduser = current_user.id
                user = User.query.get(iduser)
                user.picture_profile = newfilename
                db.session.commit()

                flash('Foto actualizado exitosamente')
                return redirect(url_for('profile_router.index'))
            else:
                flash('Allowed image types are -> png, jpg, jpeg, gif')
                return redirect(request.url)

            
profilecontroller = ProfileController()