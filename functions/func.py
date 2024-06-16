from db.categoria import CATEGORIAS


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