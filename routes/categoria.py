from flask import Blueprint, render_template, redirect, request, url_for


from db.categoria import CATEGORIAS
from db.transacao import TRANSACTIONS
from functions.func import in_categoria, find_categoria, delete_transaction_by_categoria, alter_category_in_transactions, alter_category_in_category


categoria = Blueprint("categoria", __name__)


@categoria.route("/cadastrar_categoria", methods=["GET", "POST"])
def cadastrar_categoria():
    """ 
        Função reponsável por cadatrar uma nova categoria.
        Se a solicitação for via GET ela retornará o formulário para ser preenchido.
        Senão ela vai retornar (caso não houver nenhuma falha) o formulário para cadastrar
        uma nova transação.
    """
    if request.method == "GET":
        return render_template("form_categoria.html", categorias=CATEGORIAS)
    
    categoria: str = request.json["categoria"].strip().capitalize()

    # Verificando se o campo categoria foi preenchido
    if not categoria:
        return redirect(url_for("categoria.cadastrar_categoria"))
    
    # Se a categoria já estiver cadastrada
    if in_categoria(categoria, CATEGORIAS):
        print("Erro aqui!")
        return redirect(url_for("categoria.cadastrar_categoria"))

    # Adicionando a categoria na lista de categorias 
    c = {}
    c["categoria"] = categoria
    c["id"] = len(CATEGORIAS) + 1

    CATEGORIAS.append(c)
    
    return redirect(url_for("transaction.cadastrar_transacao"))


@categoria.route("/categorias")
def categorias():
    return render_template("categorias.html", categorias=CATEGORIAS)


@categoria.route("/<int:categoria_id>/modify", methods=['GET', 'PUT'])
def modify(categoria_id):
    """
        Altera uma categoria.
        Essa alteração altera também as transações, ou seja,
        todas as transações que tinha essa categoria vão mudar para a 
        nova categoria.
    """

    if request.method == "GET":
        return render_template("form_categoria.html", categoria=find_categoria(categoria_id)[0], categoria_id=categoria_id)

    # Verificando se a categoria existe
    c = find_categoria(categoria_id)
    if not c:
        return render_template("categorias.html", categorias=CATEGORIAS)
    
    c = c[0]
    
    new_categoria = request.json
    if not new_categoria:
        return render_template("form_categoria.html", categorias=CATEGORIAS)
    
    new_categoria = new_categoria["categoria"]


    alter_category_in_transactions(TRANSACTIONS, c, new_categoria)
    alter_category_in_category(CATEGORIAS, c, new_categoria)


    return render_template("categorias.html", categorias=CATEGORIAS)


@categoria.route("/<int:categoria_id>/delete", methods=['DELETE'])
def delete(categoria_id):
    """ 
        Deleta uma categoria.
        Caso você delete uma categoria, todas as transações
        que tinha essa categoria vão ser deletadas também.
    """
    c = find_categoria(categoria_id)
    if not c:
        return render_template("categorias.html", categorias=CATEGORIAS)
        
    c = c[0]

    delete_transaction_by_categoria(TRANSACTIONS, c)

    return render_template("form_categoria.html", categorias=CATEGORIAS)
