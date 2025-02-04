def indice_maior_elemento(lista, indice=0, maior_indice=0):
    """
    Retorna o índice do maior elemento em uma lista usando recursão.

    Args:
        lista (list): Lista de números.
        indice (int): Índice atual da iteração (inicialmente 0).
        maior_indice (int): Índice do maior elemento encontrado até agora.

    Returns:
        int: Índice do maior elemento na lista.
    """
    if indice == len(lista):  # Caso base: percorreu toda a lista
        return maior_indice

    if lista[indice] > lista[maior_indice]:  # Se encontrou um novo maior
        maior_indice = indice

    return indice_maior_elemento(lista, indice + 1, maior_indice)


resultado = indice_maior_elemento([1, 5, 3, 9, 2])
print(resultado)  # Saída esperada: 3
