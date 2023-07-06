from flask import Blueprint, render_template, request, redirect, session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from trocatroca0_orm import Item, Category  # Importe as classes relevantes


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
            file = request.files['photos']
            image_blob = file.read()
            new_item = Item(person_idperson = user, name = title, brand_species = brand_species, year_acquired = year, desc = description, condition = condition, category_idcategory = category, image_blob=image_blob)
    
            #if 'photos' in request.files:
            

            # Acessar os atributos do arquivo
           

            # Salvar o conteúdo binário da imagem no atributo image_blob do objeto Item
    
            session_bd.add(new_item)
            session_bd.commit()
        return render_template('inserir_anuncio.html', anos=anos, categorias = categorias)

    else:
        # Se o usuário não estiver logado, redirecione para a página de login
        return redirect('/login')