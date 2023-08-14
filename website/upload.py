from flask import Blueprint, render_template, request, flash, redirect, url_for, send_from_directory
from . import videos, db
from .models import Video
import os
from flask_uploads import UploadNotAllowed
from flask_login import login_required, current_user
from.Whisper_Generator import transcribe_and_burn_subtitles


upload = Blueprint('upload', __name__)


@upload.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST' and 'video' in request.files:
        file = request.files['video']
        try:
            filename = videos.save(file)
            input_video_path = os.path.join('website', 'file_uploads', filename)
            transcribe_and_burn_subtitles(input_video_path)
            base_name, extension = filename.rsplit('.', 1)
            subtitled_filename = base_name + "_subtitles." + extension
            video = Video(filename=subtitled_filename, user_id=current_user.id)
            db.session.add(video)
            db.session.commit()
            flash('Video uploaded successfully!', category='success')
            return redirect(url_for('upload.display_video', filename=filename))
        except UploadNotAllowed:
            flash('Invalid video format! Please upload a valid video.', category='error')
    return render_template("home.html", user=current_user)


@upload.route('/display_video/<filename>')
@login_required
def display_video(filename):
    base_name, extension = filename.rsplit('.', 1)
    subtitled_filename = base_name + "_subtitles." + extension
    return send_from_directory('file_uploads', subtitled_filename, as_attachment=False)


@upload.route('/view_video/<filename>')
@login_required
def view_video(filename):
    return render_template("display_video.html", filename=filename)







