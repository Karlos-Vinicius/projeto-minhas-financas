from flask import Blueprint, render_template, request


transaction = Blueprint("transaction", __name__)

@transaction.route("/cadastrar_transacao", methods=["POST", "GET"])
def cadastrar_transacao():
    return render_template("cadastrar_transacao.html")