import sys
from flask import Blueprint, render_template, redirect, session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from trocatroca0_orm import Item  # Importe as classes relevantes

sys.path.append("../routes")
home_bp = Blueprint('home', __name__)

engine = create_engine('mysql+pymysql://admin:troca2023@trocatroca-db.co7hqdo9x7ll.us-east-1.rds.amazonaws.com:3306/trocatroca0')
Session = sessionmaker(bind=engine)
db_session = Session()


@home_bp.route('/home', methods=['GET', 'POST'])
def home():
    
    # Verifique se o usuário está logado
    if 'user_id' in session:
        sessio = Session()
        items = sessio.query(Item).all()
        return render_template('home.html', items=items)

    else:
        # Se o usuário não estiver logado, redirecione para a página de login
        return redirect('/login')