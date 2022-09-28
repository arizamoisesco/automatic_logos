from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, flash, redirect, url_for
import os
import secrets

UPLOAD_FOLDER = 'app/static/uploads'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

secret = secrets.token_urlsafe(32)

app = Flask(__name__)
app.secret_key = secret
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def upload_form():
    return render_template('index.html')


@app.route('/', methods = ['POST'])
def upload_file():
    if request.method == 'POST':
        if 'files' not in request.files:
            flash('No file part')
            return redirect(request.url)

        files = request.files.getlist('files')
        

        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))

        flash('Archivo(s) subido exitosamente')
        return redirect(request.url)


if __name__ == '__main__':
    app.run(debug=True)