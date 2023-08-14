from flask import Flask
from flask_uploads import UploadSet, configure_uploads
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = "database.db"


ALLOWED_VIDEO_EXTENSIONS = set(['mov', 'mp4', 'mpe', 'mpeg', 'mpg', 'mkv', 'avi', 'wmv', 'flv', 'ogv', 'webm'])

videos = UploadSet('videos', ALLOWED_VIDEO_EXTENSIONS)
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'TESTING'
    app.config['UPLOADED_VIDEOS_DEST'] = os.path.join('website', 'file_uploads')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .upload import upload
    from .auth import auth

    app.register_blueprint(upload, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    configure_uploads(app, videos)

    from .models import User, Video

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')

