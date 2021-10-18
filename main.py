from PIL import Image
import os

def redimencionar_image(image):
    
    redimencionada_img = image.resize((300, 300))
    redimencionada_img.save("logo.png", "png")
    return redimencionada_img

def logo_in_image(fondo, logo, contador):
    fondo.paste(logo, (0,0), logo)
    fondo.save(f"output/img{contador}.png", "png")
    fondo.show()
    
def rename_files(route):
    #1 introducir los arhivos dentro de una lista
    #Luego renombrar uno a uno con un ciclo
    images = os.listdir(route)
    print(images)
    contador = 0
    for image in images:
        os.rename(f"{route}/{image}", f'image{contador}.jpg')
    


#Config logo
img2 = Image.open(r"Logo-Treasure-Store.png").convert("RGBA")
img2 = redimencionar_image(img2)

images = os.listdir("input/")
numero = 0
for image in images:
    img = Image.open(rf"input/{image}")
    logo_in_image(img, img2, numero)
    numero += 1

