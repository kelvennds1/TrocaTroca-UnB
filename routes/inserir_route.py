from flask import Blueprint, render_template, request, redirect, session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from trocatroca0_orm import Item, Category  # Importe as classes relevantes
import base64



inserir_bp = Blueprint('inserir', __name__)

engine = create_engine('mysql+pymysql://admin:troca2023@trocatroca-db.co7hqdo9x7ll.us-east-1.rds.amazonaws.com:3306/trocatroca0')
Session = sessionmaker(bind=engine)
session_bd = Session()

anos = [x for x in range(2005,2024)]
anos = sorted(anos,reverse=True)

@inserir_bp.route('/inserir', methods=['GET', 'POST'])
def inserir():
    if 'user_id' in session:
        categorias = session_bd.query(Category).all()
        if request.method == 'POST':
            user = session['user_id']  
            title = request.form['title']
            description = request.form['description']
            category = request.form['category']
            if request.form['brand']:
                brand_species = request.form['brand']
            else:
                brand_species = request.form['race']
            condition = request.form['condition']
            year = request.form['year']
    
            
            new_item = Item(person_idperson = user, name = title, brand_species = brand_species, year_acquired = year, desc = description, condition = condition, category_idcategory = category)
    
            #if 'photos' in request.files:
            file = request.files['photos']

            # Acessar os atributos do arquivo
            filename = file.filename
            file_type = file.content_type
            file_data = file.read()
            img_64 = base64.b64encode(file_data)
            #.decode('utf-8')
            print(img_64)

            # Salvar o conteúdo binário da imagem no atributo image_blob do objeto Item
            new_item.image_blob = img_64

            session_bd.add(new_item)
            session_bd.commit()
        return render_template('inserir_anuncio.html', anos=anos, categorias = categorias)

    else:
        # Se o usuário não estiver logado, redirecione para a página de login
        return redirect('/login')