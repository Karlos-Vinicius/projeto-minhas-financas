def in_categoria(categoria: str | int, categorias: list[dict]) -> True | False:
    """
        Função usada para verificar se uma categoria está presente na lista de gategorias
    """
    for c in categorias:
        if categoria == c["categoria"]: 
            return True
        
    return False