from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime
from functions.func import in_categoria, find_transaction, edit_transaction, delete_transaction


from db.transacao import TRANSACTIONS
from db.categoria import CATEGORIAS


transaction = Blueprint("transaction", __name__)

@transaction.route("/")
def index(): 
    return render_template("transactions.html", transactions=TRANSACTIONS)


@transaction.route("/cadastrar_transacao", methods=["POST", "GET"])
def cadastrar_transacao():
    """
    Função reponsável por cadastrar uma nova transação no banco de dados.

    Caso a solicitação seja via GET ela retornará o formulário para ser preenchido.
    Caso contrário ela retornará (se não houver nenhuma falha) o tabela, por onde o usuário
    poderar visualizar os dads de suas transações.
    """
    if request.method == "GET":
        return render_template("form_transacao.html", categorias=CATEGORIAS)

    transacao = request.json

    if not (transacao["valor"] and transacao["categoria"]): 
        # Conferindo os campos em que o preenchimento é obrigatório
        print("Muito errado errado: ", transacao)
        return redirect(url_for("transaction.cadastrar_transacao"))
    
    if not in_categoria(categoria=transacao["categoria"], categorias=CATEGORIAS):
        # Se a categoria não estiver no banco de dados
        return redirect(url_for("transaction.cadastrar_transacao"))
    
    time = datetime.now().strftime("%d/%m/%Y %H:%M")
    
    t = {"categoria": transacao["categoria"], "descricao": transacao["descricao"], "valor": transacao["valor"], "momento": time}

    TRANSACTIONS.append(t)

    return redirect(url_for("transaction.index", transactions=TRANSACTIONS))


@transaction.route("/edit_transactions")
def edit_transactions():
    """
        Função responsável por retornar a tabela com a coluna Ações, por onde o usuário
        poderá editar ou deletar uma transação
    """
    return render_template("edit_transactions.html", transactions=TRANSACTIONS)


@transaction.route("/<int:transaction_id>/edit", methods=["GET", "PUT"])
def edit(transaction_id):
    """
        Função responsável por enviar o formulário para editar uma transação
        e por efetivamente editar uma transação
    """
    if request.method == "GET":
        return render_template("form_transacao.html", transaction=find_transaction(TRANSACTIONS, transaction_id)[0], categorias=CATEGORIAS)
    
    # Edita a transação
    edit_transaction(TRANSACTIONS, transaction_id, request.json)

    return render_template("transactions.html", transactions=TRANSACTIONS)


@transaction.route("/<int:transaction_id>/delete", methods=["DELETE"])
def delete(transaction_id):
    """
        Responsável por deletar uma transação com base no seu id
    """

    delete_transaction(TRANSACTIONS, transaction_id)

    return render_template("transactions.html", transactions=TRANSACTIONS)