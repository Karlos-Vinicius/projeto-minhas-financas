from db.categoria import CATEGORIAS
from db.transacao import TRANSACTIONS


def in_categoria(categoria: str | int, categorias: list[dict]) -> True | False:
    """
        Função usada para verificar se uma categoria está presente na lista de gategorias.
    """
    for c in categorias:
        if categoria == c["categoria"]: 
            return True
        
    return False


def find_categoria(categoria_id: int) -> list[str]:
    """
        Retorna a categoria combase no seu id.
    """
    return [c["categoria"] for c in CATEGORIAS if c["id"] == categoria_id]


def delete_transaction_by_categoria(transactions: list[dict], categoria: str, i: int = 0) -> None:
    """
        Função recursiva que deleta todas as transações que tenha essa essa categoria.
    """
    if i >= len(transactions):
        return None
    
    if transactions[i]["categoria"] == categoria:
        del transactions[i]
    
    else: 
        i += 1

    delete_transaction_by_categoria(transactions, categoria, i)


def delete_cateogry_by_id(categorys: list[dict], category_id: int, i: int = 0) -> None:
    """
        Função recursiva responsável por deletar uma categoria com base no seu id.
        Lembre-se de usá-la depois de deletar todas as transações com essa categoria.
    """
    if i >= len(categorys):
        raise

    if categorys[i]["id"] == category_id:
        del categorys[i]
        return None
    
    i += 1

    delete_cateogry_by_id(categorys, category_id, i)

def alter_category_in_transactions(transactions: list[dict], category: str, new_category: str, i: int = 0) -> None:
    """
        Altera uma categoria de uma transação.
    """
    if i >= len(transactions):
        return None
    
    if transactions[i]["categoria"] == category:
        transactions[i]["categoria"] = new_category
    
    i += 1

    alter_category_in_transactions(transactions, category, new_category, i)

def alter_category_in_category(categorys: list[dict], category: str, new_category: str, i: int = 0):
    """
        Função recursiva que altera a categoria para a nova categoria.
    """
    if i >= len(categorys):
        return None
    
    if categorys[i]["categoria"] == category:
        categorys[i]["categoria"] = new_category
        return None

    i += 1

    alter_category_in_category(categorys, category, new_category, i)