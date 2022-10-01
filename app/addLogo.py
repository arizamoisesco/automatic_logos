from PIL import Image
import os

class AddLogo():

    def __init__(self):
        self.company_logo = self.redimencionar_image(Image.open(r"Logo-Treasure-Store.png").convert("RGBA"))
        self.dir_images_uploads = os.listdir("app/static/uploads/")
        self.image_code = 0
    
    def redimencionar_image(self, image):
        
        redimencionada_img = image.resize((300, 300))
        redimencionada_img.save("logo.png", "png")
        return redimencionada_img

    def logo_in_image(self, fondo, contador):
        fondo.paste(self.company_logo, (0,0), self.company_logo)
        fondo.save(f"app/static/downloads/img{contador}.png", "png")
        return print("Tarea completada")
        
    def rename_files(self, route):
        #1 introducir los arhivos dentro de una lista
        #Luego renombrar uno a uno con un ciclo
        images = os.listdir(route)
        print(images)
        contador = 0
        for image in images:
            os.rename(f"{route}/{image}", f'image{contador}.jpg')
        


