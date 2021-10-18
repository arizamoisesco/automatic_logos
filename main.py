from PIL import Image

def redimencionar_image(image):
    
    redimencionada_img = image.resize((300, 300))
    redimencionada_img.save("logo.png", "png")
    return redimencionada_img

def logo_in_image(fondo, logo):
    x, y = fondo.size
    print(x)
    fondo.paste(logo, (0,0), logo)
    fondo.save("output/test.png", "png")
    fondo.show()
    

img = Image.open(r"rubor.jpg")
img2 = Image.open(r"Logo-Treasure-Store.png").convert("RGBA")
img2 = redimencionar_image(img2)
logo_in_image(img, img2)