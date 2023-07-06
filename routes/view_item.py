import sys
from flask import Blueprint, render_template, redirect, session, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from trocatroca0_orm import Item # Importe as classes relevantes

sys.path.append("../routes")
itens_bp = Blueprint('itens_bp', __name__)

engine = create_engine('mysql+pymysql://admin:troca2023@trocatroca-db.co7hqdo9x7ll.us-east-1.rds.amazonaws.com:3306/trocatroca0')
Session = sessionmaker(bind=engine)
db_session = Session()



@itens_bp.route("/itens")
def visualizar_itens():
    user_id = request.args.get('user_id')
    
    session = Session()

    
    # Execute a query para obter todos os itens do usuário logado, ordenados pela data mais recente
    itens = session.query(Item).filter_by(person_idperson=user_id).order_by(Item.time_created.desc()).all()

    return render_template("visualizar_itens.html", items=itens)
