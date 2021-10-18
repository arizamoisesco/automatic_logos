from PIL import Image

def redimencionar_image(image):
    
    redimencionada_img = image.resize((100, 100))
    redimencionada_img.save("logo.png", "png")

img = Image.open("city.jpg")
redimencionar_image(img)