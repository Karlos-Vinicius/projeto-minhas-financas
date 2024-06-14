from flask import Blueprint, render_template, request


transaction = Blueprint("transaction", __name__)

@transaction.route("/")
def index(): 
    return render_template("transactions.html")

@transaction.route("/cadastrar_transacao", methods=["POST", "GET"])
def cadastrar_transacao():
    return render_template("cadastrar_transacao.html")