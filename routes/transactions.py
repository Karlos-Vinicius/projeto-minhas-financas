from flask import Blueprint, render_template, request


from db.transacao import TRANSACTIONS


transaction = Blueprint("transaction", __name__)

@transaction.route("/")
def index(): 
    return render_template("transactions.html", transactions=TRANSACTIONS)

@transaction.route("/cadastrar_transacao", methods=["POST", "GET"])
def cadastrar_transacao():
    return render_template("cadastrar_transacao.html")

@transaction.route("/cadastrar_categoria", methods=["GET", "POST"])
def cadastrar_categoria():
    return render_template("cadastrar_categoria.html")