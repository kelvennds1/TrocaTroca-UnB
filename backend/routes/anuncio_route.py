from flask import Blueprint, render_template, request, redirect
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from trocatroca0_orm import Item  # Importe as classes relevantes

sys.path.append("../routes")
anuncio_bp = Blueprint('anuncio', __name__)

engine = create_engine('mysql+pymysql://admin:troca2023@trocatroca-db.co7hqdo9x7ll.us-east-1.rds.amazonaws.com:3306/trocatroca0')
Session = sessionmaker(bind=engine)
sessio = Session()

# Nota: me parece que isso foi inutilizado e esta quebrado



@anuncio_bp.route('/anuncio/<int:item_id>', methods=['GET', 'POST'])
def anuncio(item_id):
    db = Session()
    item = db.query(Item).filter_by(iditem=item_id).filter(Item.name != "DONATION_PLACEHOLDER").first()
    all_items = db.query(Item).filter(Item.name != "DONATION_PLACEHOLDER").all()

    return render_template('anuncio.html', item=item, items=all_items)

