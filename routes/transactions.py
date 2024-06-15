from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime


from db.transacao import TRANSACTIONS
from db.categoria import CATEGORIAS


transaction = Blueprint("transaction", __name__)

@transaction.route("/")
def index(): 
    return render_template("transactions.html", transactions=TRANSACTIONS)


@transaction.route("/cadastrar_transacao", methods=["POST", "GET"])
def cadastrar_transacao():
    if request.method == "GET":
        return render_template("cadastrar_transacao.html", categorias=CATEGORIAS)
    
    transacao = request.json

    if not (transacao["valor"] and transacao["categoria"]): 
        return render_template("cadastrar_transacao.html", categorias=CATEGORIAS)
    
    t = {"categoria": transacao["categoria"], "descricao": transacao["descricao"], "valor": transacao["valor"], "momento": datetime.now()}

    TRANSACTIONS.append(t)

    return redirect(url_for("transaction.index", transactions=TRANSACTIONS))


@transaction.route("/cadastrar_categoria", methods=["GET", "POST"])
def cadastrar_categoria():
    if request.method == "GET":
        return render_template("cadastrar_categoria.html")
    
    categoria = request.json

    if not categoria:
        return render_template("cadastrar_categoria.html")
    
    c = categoria["categoria"]
    CATEGORIAS.append(c)
    
    return redirect(url_for("transaction.cadastrar_transacao"))