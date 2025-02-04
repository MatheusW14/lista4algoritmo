def soma_lista_aninhada(lista):
    """
    Calcula a soma de todos os números em uma lista, mesmo se estiverem dentro de sublistas.

    Args:
        lista (list): Lista possivelmente aninhada contendo números.

    Returns:
        int: Soma de todos os números.
    """
    soma = 0
    for elemento in lista:
        if isinstance(
            elemento, list
        ):  # Se for uma lista, chama a função recursivamente
            soma += soma_lista_aninhada(elemento)
        else:  # Se for um número, adiciona diretamente à soma
            soma += elemento
    return soma


resultado = soma_lista_aninhada([1, [2, 3], [4, [5]]])
print(resultado)
