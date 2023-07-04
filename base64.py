import base64

IMG_PATH = ''

with open( IMG_PATH, "rb") as image_file:
## USA ESSE ENCODING P SALVAR A STRING NO BANCO
    img_64 = base64.b64encode(image_file.read()) 
print(img_64) # string b'[...]

# teste fetch e display de item com /itemunicoid2' e mudando o iditem