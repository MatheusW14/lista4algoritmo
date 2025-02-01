def reverter_caracteres(s):
    """
    Reverte os caracteres de uma string de forma recursiva.

    Args:
        s (str): A string a ser revertida.

    Returns:
        str: A string com os caracteres em ordem reversa.

    Exemplo:
        >>> reverter_caracteres("abc")
        'cba'
    """
    if len(s) == 0:  # Se a string estiver vazia,
        return ""
    return s[-1:] + reverter_caracteres(
        s[:-1]
    )  # Concatena o último caractere com a string restante invertida


texto = input("Digite um texto:")
texto_revertido = reverter_caracteres(texto)
print(f"O texto revertido é: {texto_revertido}")
