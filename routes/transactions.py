from flask import Blueprint, render_template, request, redirect, url_for


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
    
    return redirect(url_for("transaction.index", transactions=TRANSACTIONS))

@transaction.route("/cadastrar_categoria", methods=["GET", "POST"])
def cadastrar_categoria():
    if request.method == "GET":
        return render_template("cadastrar_categoria.html")
    
    return redirect(url_for("transaction.cadastrar_transacao"))