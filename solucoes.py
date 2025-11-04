def sao_anagramas(string1, string2):
    # TODO: Implementar a lógica
    pass

def cifra_de_cesar(texto, deslocamento):
    # TODO: Implementar a lógica
    pass

def encontrar_maior_palavra(frase):
    if not isinstance(frase, str):
        raise TypeError("A entrada deve ser string.")

    if not frase.strip():
        return ""

    palavras = frase.split()

    # seleciona apenas os caracteres alfabeticos e obtem a palavra de maior tamanho
    maior_palavra = max(palavras, key=lambda p: len(''.join(filter(str.isalpha, p))))

    return ''.join(filter(str.isalpha, maior_palavra))