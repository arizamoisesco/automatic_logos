from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, flash, redirect, url_for
import os

UPLOAD_FOLDER = 'app/static/uploads'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    #file = filename.split('.')
    #if file[1] in ALLOWED_EXTENSIONS:
    #    return True
    #return False
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_file():
    return render_template('index.html')


@app.route('/upload', methods = ['GET','POST'])
def uploadfile():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        filename = secure_filename(file.filename)
        print(filename)

        if file.filename == '':
           flash('No ha seleccionado archivo')
           return redirect(request.url) 
        
        if file and allowed_file(filename):
            
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            #file.save(f"{UPLOAD_FOLDER}/{filename}")
            #return redirect(url_for('download_file', name=filename))
            return 'Archivo subido exitosamente'

if __name__ == '__main__':
    app.run(debug=True)