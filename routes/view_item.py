from flask import Flask, render_template
from trocatroca0_orm import Item  # Importe o modelo Item correspondente à tabela do banco de dados

app = Flask(__name__)


@app.route("/itens")
def visualizar_itens():
    
    # Execute a query para obter todos os itens do usuário logado, ordenados pela data mais recente
    itens = Item.query.filter_by(user_id=Session["user_id"]).order_by(Item.data.desc()).all()

    return render_template("visualizar_itens.html", itens=itens)
