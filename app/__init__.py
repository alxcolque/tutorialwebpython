__version__ = "0.1"
from flask import Flask
import secrets

UPLOAD_FOLDER = 'app/static/img/uploads/'
#app = Flask('app')

app = Flask(__name__, template_folder="views")

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

secret = secrets.token_urlsafe(32)
app.config['SECRET_KEY'] = secret

app.debug = True

from app.routes.main_router import main_router
app.register_blueprint(main_router)
