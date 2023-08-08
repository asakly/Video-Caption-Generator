from flask import Blueprint, render_template, request, flash
from . import videos
from flask_uploads import UploadNotAllowed

upload = Blueprint('upload', __name__)


@upload.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST' and 'video' in request.files:
        file = request.files['video']
        try:
            filename = videos.save(file)
            flash('Video uploaded successfully!', category='success')
            return f'Video saved as {filename}'
        except UploadNotAllowed:
            flash('Invalid video format! Please upload a valid video.', category='error')
    return render_template("home.html")



