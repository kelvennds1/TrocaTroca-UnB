import sys
from flask import Blueprint, render_template, request, redirect, session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import jsonify
from trocatroca0_orm import Person  # Importe as classes relevantes

sys.path.append("../routes")
login_bp = Blueprint('login', __name__)

engine = create_engine('mysql+pymysql://admin:troca2023@trocatroca-db.co7hqdo9x7ll.us-east-1.rds.amazonaws.com:3306/trocatroca0')
Session = sessionmaker(bind=engine)
db_session = Session()


@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Obtenha os dados do formulário de login
        hash_email = request.form['hash_email']
        hash_passw = request.form['hash_passw']

        # Consulte o banco de dados para verificar se o usuário existe
        pessoa = db_session.query(Person).filter_by(email=hash_email).first()

        if pessoa and pessoa.passw == hash_passw: # type: ignore
            # Autenticação bem-sucedida
            session['user_id'] = pessoa.idperson
            session['username'] = pessoa.name

            # Crie um dicionário com os dados a serem serializados

            # Serialize o dicionário para JSON e retorne a resposta
            return redirect('/home')

        else:
            # Autenticação falhou
            return jsonify({'error': 'Authentication failed'})

    return render_template('login.html', error=False)
