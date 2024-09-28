import base64

# IMG_PATH = 'tears-seulgi.jpg'
IMG_PATH = input()

with open( IMG_PATH, "rb") as image_file:
## USA LINHAS 8-9 P SALVAR A STRING NO BANCO
    img_64 = base64.b64encode(image_file.read()) 
    img_64 = img_64.decode('utf-8')
    
    
print(img_64) # string b'[...]

# teste fetch e display de item com /itemunicoid<IDITEM>' e mudando o iditem

