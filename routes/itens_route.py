from flask import Flask, render_template, request, redirect, session , jsonify, Blueprint
from sqlalchemy import create_engine, cast, select
from sqlalchemy.orm import sessionmaker
from trocatroca0_orm import *
import pytz
from datetime import datetime, timedelta
from time import sleep
import sys
from flask import request

engine = create_engine('mysql+pymysql://admin:troca2023@trocatroca-db.co7hqdo9x7ll.us-east-1.rds.amazonaws.com:3306/trocatroca0')
Session = sessionmaker(bind=engine)
db_session = Session()

sys.path.append("../routes")
itens_bp = Blueprint('itens', __name__)

@itens_bp.route("/itens")
def visualizar_itens():
    user_id = request.args.get('user_id')
    db = Session()
    #  Execute a query para obter todos os itens do usuário logado, ordenados pela data mais recente
    print(db.query(Item).filter_by(person_idperson=user_id).count())
    itens = db.query(Item).filter_by(person_idperson=user_id).order_by(Item.time_created.desc()).all()
    print(itens)

    return render_template("visualizar_itens.html", items=itens)
