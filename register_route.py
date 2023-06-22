from flask import Blueprint, render_template, request, redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from trocatroca0_orm import Person  # Importe as classes relevantes

registro_bp = Blueprint('registro', __name__)

engine = create_engine('mysql+pymysql://admin:troca2023@trocatroca-db.co7hqdo9x7ll.us-east-1.rds.amazonaws.com:3306/trocatroca0')
Session = sessionmaker(bind=engine)
session = Session()
ultima_person = session.query(Person).order_by(Person.idperson.desc()).first()
if (ultima_person):
    ultimo_id = ultima_person.idperson

@registro_bp.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        # Obtenha os dados do formulário de registro
        registration = request.form['registration']
        passw = request.form['passw']
        name = request.form['name']
        passw = request.form['passw']
        email = request.form['email']

        # Crie uma nova instância da classe Person com os dados do formulário
        nova_person = Person(idperson=ultimo_id+1, registration=registration, passw=passw, name=name, email = email)

        # Inicie uma nova sessão do SQLAlchemy
        try:
            # Adicione a nova person à sessão
            session.add(nova_person)

            # Faça o commit da sessão para salvar a nova person no banco de dados
            session.commit()

            # Redirecione para uma página de sucesso ou faça algo similar
            return redirect('/login')

        except Exception as e:
            # Lide com possíveis erros durante o registro
            session.rollback()
            print(f"Erro durante o registro: {str(e)}")
            return render_template('registrar.html', error=True)

        finally:
            # Feche a sessão do SQLAlchemy
            session.close()

    return render_template('registrar.html', error=False)
