from flask import Blueprint, render_template, redirect, request, url_for


from db.categoria import CATEGORIAS
from functions.func import in_categoria


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