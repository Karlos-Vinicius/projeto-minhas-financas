from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime
from functions.func import in_categoria


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
        return render_template("cadastrar_transacao.html", categorias=CATEGORIAS)

    transacao = request.json

    if not (transacao["valor"] and transacao["categoria"]): 
        # Conferindo os campos em que o preenchimento é obrigatório
        print("Muito errado errado: ", transacao)
        return render_template("cadastrar_transacao.html", categorias=CATEGORIAS)
    
    if not in_categoria(categoria=transacao["categoria"], categorias=CATEGORIAS):
        # Se a categoria não estiver no banco de dados
        print(transacao["categoria"])
        print("Aqui deu errado: ", transacao)
        return render_template("cadastrar_transacao.html", categorias=CATEGORIAS)
    
    time = datetime.now().strftime("%d/%m/%Y %H:%M")
    
    t = {"categoria": transacao["categoria"], "descricao": transacao["descricao"], "valor": transacao["valor"], "momento": time}

    TRANSACTIONS.append(t)

    return redirect(url_for("transaction.index", transactions=TRANSACTIONS))


@transaction.route("/cadastrar_categoria", methods=["GET", "POST"])
def cadastrar_categoria():
    """ 
        Função reponsável por cadatrar uma nova categoria.
        Se a solicitação for via GET ela retornará o formulário para ser preenchido.
        Senão ela vai retornar (caso não houver nenhuma falha) o formulário para cadastrar
        uma nova transação.
    """
    if request.method == "GET":
        return render_template("cadastrar_categoria.html", categorias=CATEGORIAS)
    
    categoria: str = request.json["categoria"].strip().capitalize()

    # Verificando se o campo categoria foi preenchido
    if not categoria:
        return redirect(url_for("transaction.cadastrar_categoria"))
    
    # Se a categoria já estiver cadastrada
    if in_categoria(categoria, CATEGORIAS):
        print("Erro aqui!")
        return redirect(url_for("transaction.cadastrar_categoria"))

    # Adicionando a categoria na lista de categorias 
    c = {}
    c["categoria"] = categoria
    c["id"] = len(CATEGORIAS) + 1

    CATEGORIAS.append(c)
    
    return redirect(url_for("transaction.cadastrar_transacao"))