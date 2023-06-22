from flask import Blueprint, render_template, request, redirect, session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from trocatroca0_orm import Person  # Importe as classes relevantes

login_bp = Blueprint('login', __name__)

engine = create_engine('mysql+pymysql://<username>:<password>@<host>:<port>/<database>')
Session = sessionmaker(bind=engine)
db_session = Session()

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Obtenha os dados do formulário de login
        email = request.form['email']
        password = request.form['password']

        # Consulte o banco de dados para verificar se o usuário existe
        person = db_session.query(Person).filter_by(email=email).first()

        if person and person.password == password:
            # Autenticação bem-sucedida
            session['user_id'] = person.id
            return redirect('/dashboard')
        else:
            # Autenticação falhou
            return render_template('login.html', error=True)

    return render_template('login.html', error=False)
