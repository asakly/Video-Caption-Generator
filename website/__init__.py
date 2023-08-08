from flask import Flask
from flask_uploads import UploadSet, configure_uploads


ALLOWED_VIDEO_EXTENSIONS = set(['mov', 'mp4', 'mpe', 'mpeg', 'mpg', 'mkv', 'avi', 'wmv', 'flv', 'ogv', 'webm'])

videos = UploadSet('videos', ALLOWED_VIDEO_EXTENSIONS)
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'TESTING'
    app.config['UPLOADED_VIDEOS_DEST'] = r'C:\Users\anwar\Desktop\Projects\Video_Caption_Generator\file_uploads'

    from .upload import upload
    from .auth import auth

    app.register_blueprint(upload, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    configure_uploads(app, videos)

    return app

