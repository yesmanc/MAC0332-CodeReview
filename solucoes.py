def sao_anagramas(string1, string2):
    # TODO: Implementar a lógica
    pass

def cifra_de_cesar(texto, deslocamento):
    if not isinstance(texto, str):
        raise TypeError("O texto deve ser uma string.")
    if not isinstance(deslocamento, int):
        raise TypeError("O deslocamento deve ser um inteiro.")
    
    texto_final = ""
    
    for char in texto:
        """ Obtem o caractere novo com base nos 26 caracteres 
            alfabeticos (como se fosse uma lista circular), diferenciando
            entre maiusculas e minusculas, e coloca esse caractere no 
            texto final.
        """

        if 'a' <= char <= 'z':
            char_ord = ord('a') + (ord(char) - ord('a') + deslocamento) % 26
            texto_final += chr(char_ord)

        elif 'A' <= char <= 'Z':
            char_ord = ord('A') + (ord(char) - ord('A') + deslocamento) % 26
            texto_final += chr(char_ord)

        else:
            texto_final += char

    return texto_final

def encontrar_maior_palavra(frase):
    if not isinstance(frase, str):
        raise TypeError("A entrada deve ser string.")

    if not frase.strip():
        return ""

    palavras = frase.split()

    # seleciona apenas os caracteres alfabeticos e obtem a palavra de maior tamanho
    maior_palavra = max(palavras, key=lambda p: len(''.join(filter(str.isalpha, p))))

    return ''.join(filter(str.isalpha, maior_palavra))
