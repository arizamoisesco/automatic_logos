from importlib.resources import path
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, flash, redirect, send_from_directory, url_for, send_file

from PIL import Image

from addLogo import AddLogo

import os
import secrets
import zipfile

UPLOAD_FOLDER = 'app/static/uploads'
DOWNLOAD_FOLDER = 'static/downloads/'
LOGO_COMPANY = 'app/static/company_logo'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

secret = secrets.token_urlsafe(32)

app = Flask(__name__)
app.secret_key = secret
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
app.config['LOGO_COMPANY'] = LOGO_COMPANY

add_logo = AddLogo()


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def upload_form():
    return render_template('index.html')


@app.route('/', methods = ['POST'])
def upload_file():
     if request.method == 'POST':
    ######Upload Logo #######
   
        if 'logo' not in request.files:
            flash('No se encontro logo de la empresa')
            return redirect(request.url)
        
        company_logo = request.files['logo']
        print(company_logo)
        company_logo_filename = secure_filename(company_logo.filename)
        print(company_logo_filename)
        company_logo.save(os.path.join(app.config['LOGO_COMPANY'],company_logo_filename))
        print("Logramos subir el logo de la compañia" )


    ###### Upload files #####

        if 'files' not in request.files:
            flash('No file part')
            return redirect(request.url)

        files = request.files.getlist('files')
        
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        
        flash('Archivo(s) subido exitosamente')
        

        logo = rf"app/static/company_logo/{company_logo_filename}"
        img2 = Image.open(logo).convert("RGBA")
        img2 = redimencionar_image(img2)

        images = os.listdir(f"app/static/uploads/")
        numero = 0
        for image in images:
            img = Image.open(rf"app/static/uploads/{image}")
            logo_in_image(img, img2, numero)
            numero += 1

        return redirect(request.url)


@app.route('/download')
def download_file():

     return send_from_directory('static/', 'archive.zip', as_attachment=True)
     



#####Procesamiento de imagen######
def redimencionar_image(image):
    
    redimencionada_img = image.resize((200, 200))
    redimencionada_img.save("logo.png", "png")
    return redimencionada_img

def logo_in_image(fondo, logo, contador):
    fondo.paste(logo, (0,0), logo)
    fondo.save(f"app/static/downloads/img{contador}.png", "png")
    compress_file()
    #fondo.show()
    
def rename_files(route):

    images = os.listdir(route)
    print(images)
    contador = 0
    for image in images:
        os.rename(f"{route}/{image}", f'image{contador}.jpg')
    
############# Comprimiendo las imágenes descargadas ##############
def compress_file():
    file_zip = zipfile.ZipFile("app/static/archive.zip", "w")

    for folder, subfolder, files in os.walk('app/static/downloads'):

        for file in files:
            if file.endswith('.png'):
                file_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), 'app/static/downloads'), compress_type = zipfile.ZIP_DEFLATED)
    file_zip.close()

if __name__ == '__main__':
    app.run(debug=True)