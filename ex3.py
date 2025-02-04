def contar_caracteres(s, c):
    """
    Conta quantas vezes um caractere aparece em uma string, usando recursão.

    Args:
        s (str): A string onde será feita a contagem.
        c (str): O caractere a ser contado.

    Returns:
        int: Número de vezes que o caractere aparece na string.
    """
    if not s:  # Caso base: se a string estiver vazia, retorna 0
        return 0
    return (1 if s[0] == c else 0) + contar_caracteres(s[1:], c)


# Exemplo de uso
resultado = contar_caracteres("banana", "a")
print(resultado)
