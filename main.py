# -*- coding: utf-8 -*-

# ---------------------------------------- Importar as classes relevantes ------------------------------------------------------
from flask import Flask, render_template, request, redirect, session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from routes.register_route import registro_bp # Importe o blueprint de registro
from routes.login_route import login_bp
from routes.logout_route import logout_bp
from routes.home_route import home_bp
from routes.swap_route import swap_bp
from routes.explorar_route import explorar_bp
from routes.anuncio_route import anuncio_bp
from routes.inserir_route import inserir_bp
from trocatroca0_orm import *
import ssl
import base64
#------------------------------------------------ Criar App -------------------------------------------------------------
app = Flask(__name__, template_folder='templates')

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
app.register_blueprint(logout_bp)
app.register_blueprint(home_bp)
app.register_blueprint(swap_bp)
app.register_blueprint(explorar_bp)
app.register_blueprint(anuncio_bp)
app.register_blueprint(inserir_bp)
# app.register_blueprint(explorar_bp)


app.secret_key = '342342354525351sadad1eqd'  # Chave secreta para gerar sessões seguras

# Configure o banco de dados
engine = create_engine('mysql+pymysql://admin:troca2023@trocatroca-db.co7hqdo9x7ll.us-east-1.rds.amazonaws.com:3306/trocatroca0')
Session = sessionmaker(bind=engine)


@app.route('/explorar', methods=['GET', 'POST'])
@app.route('/explorar/<tipo>', methods=['GET', 'POST'])
def explorar(tipo=None):
    sessio = Session()
    if tipo:
        # Filtrar os itens por tipo (troca ou doação)
        items = sessio.query(Item).filter_by(item_type=tipo).filter(Item.name != "DONATION_PLACEHOLDER").all()
    else:
        # Carregar todos os itens
        items = sessio.query(Item).filter(Item.name != "DONATION_PLACEHOLDER").all()
    return render_template('explorar.html', items=items)

    
# testa display de item, imagem
@app.route('/itemunicoid<int:iditem>')
def display_item(iditem):
    db = Session()
    item = db.query(Item).filter_by(iditem=iditem).first()
    db.close()
    try:
        image_decoded = item.image_blob.decode('utf-8')
        #image_decoded = base64.b64decode(image_decoded)
    except Exception as e:
        print(e)
        image_decoded ='"img 🫥"'
    return render_template('item.html', item=item, image_base64=image_decoded)
    

# pagina de anuncio de troca 

if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('localhost.pem', 'localhost-key.pem')
    app.run(debug=True, host='0.0.0.0')



