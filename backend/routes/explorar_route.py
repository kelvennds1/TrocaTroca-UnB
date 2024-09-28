from flask import Blueprint, render_template
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from trocatroca0_orm import Item, Person  # Importe as classes relevantes

sys.path.append("../routes")
explorar_bp = Blueprint('explorar', __name__)

engine = create_engine('mysql+pymysql://admin:troca2023@trocatroca-db.co7hqdo9x7ll.us-east-1.rds.amazonaws.com:3306/trocatroca0')
Session = sessionmaker(bind=engine)
sessio = Session()


@explorar_bp.route('/explorar', methods=['GET', 'POST'])
@explorar_bp.route('/explorar/<tipo>', methods=['GET', 'POST'])
def explorar(tipo=None):
    sessio = Session()
    pessoas = sessio.query(Person).all()
    if tipo:
        # Filtrar os itens por tipo (troca ou doação)
        items = sessio.query(Item).filter_by(item_type=tipo, ).filter(Item.name != "DONATION_PLACEHOLDER").all()
    else:
        # Carregar todos os itens
        items = sessio.query(Item).filter(Item.name != "DONATION_PLACEHOLDER").all()
    return render_template('explorar.html', items=items,pessoas=pessoas)

