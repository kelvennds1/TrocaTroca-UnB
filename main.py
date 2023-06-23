# ---------------------------------------- Importar as classes relevantes ------------------------------------------------------
from flask import Flask, render_template, request, redirect, session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from routes.register_route import registro_bp # Importe o blueprint de registro
from routes.login_route import login_bp
from routes.home_route import home_bp
from trocatroca0_orm import *

#------------------------------------------------ Criar App -------------------------------------------------------------
app = Flask(__name__)

#-------------------------------------------- Importando Rotas ------------------------------------------------------------
@app.before_request
def activate_service_worker():
    # Definir as configurações para o Service Worker
    request.environ['wsgi.url_scheme'] = 'https'
    request.environ['HTTP_SERVICE_WORKER_ALLOWED'] = '/'

@app.route('/', methods=['GET', 'POST'])
def index():
    # Rota principal
    return render_template('index.html')

app.register_blueprint(registro_bp)  # Registrar o blueprint de registro na aplicação Flask
app.register_blueprint(login_bp)
app.register_blueprint(home_bp)


app.secret_key = '342342354525351sadad1eqd'  # Chave secreta para gerar sessões seguras

# Configure o banco de dados
engine = create_engine('mysql+pymysql://admin:troca2023@trocatroca-db.co7hqdo9x7ll.us-east-1.rds.amazonaws.com:3306/trocatroca0')
Session = sessionmaker(bind=engine)

@app.route('/logout')
def logout():
    # Remova as informações do usuário da sessão
    session.pop('user_id', None)
    session.pop('username', None)
    # Redirecione para a página de login
    return redirect('/login')
    
@app.route('/inserir')
def inserir():
    return render_template('inserir_anuncio.html')



app.route('/insert')
def insert_item():
    image_path = 'path_to_image.jpg'  # Replace with the path to your image file
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
        image_base64 = base64.b64encode(image_data).decode('utf-8')

    item = Item(name='Example Item', image_base64=image_base64)
    db.session.add(item)
    db.session.commit()
    return 'Item inserted successfully!'

@app.route('/blob')
def display_items():
    db = Session()
    # items = db.query(Item).all()
    item = db.query(Item).filter_by(iditem = 2)
    db.close()
    # image_blob = item.image_blob

    # try:
    #     # image_blob = cast(item.image_blob, LargeBinary)
    #     # image_blob = item.image_blob.value if item.image_blob is not None else None
    #     # str_base64 = image_blob.decode('utf-8') 
    # except:
    #     print('!!!error in img decoding')
    #     str_base64 = 'img 🫥'
    try:

        image_blob = item.image_blob.decode('utf-8')
    except:
        image_blob = 'img 🫥'

    return render_template('items.html', items=items)
    # return render_template('item.html', item=item, image_base64=image_blob)
    
# testa display de item, imagem
@app.route('/itemunicoid2')
def display():
    db = Session()
    item = db.query(Item).filter_by(iditem = 2 ).first()
    db.close()
    try:
        image_decoded = item.image_blob.decode('utf-8')
    except:
        image_decoded ='"img 🫥"'
    return render_template('item.html', item=item, image_base64=image_decoded)
    

@app.route('/items')
def display_item():
    db = Session() 
    # items = db.query(Item).all()
    item = db.query(Item).first()

    # image_blob = item.image_blob

    # try:
    #     # image_blob = cast(item.image_blob, LargeBinary)
    #     # image_blob = item.image_blob.value if item.image_blob is not None else None
    #     # str_base64 = image_blob.decode('utf-8') 
    # except:
    #     print('!!!error in img decoding')
    #     str_base64 = 'img 🫥'
    try:

        image_blob = item.value(item.first().image_blob)
        image_blob = item.image_blob.decode('utf-8')
    except:
        image_blob = 'img 🫥'

    # return render_template('items.html', items=items)
    return render_template('item.html', item=item, image_base64=image_blob)
    

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')


