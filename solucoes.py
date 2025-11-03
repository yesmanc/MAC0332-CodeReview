def sao_anagramas(string1, string2):
    # TODO: Implementar a lógica
    pass

def cifra_de_cesar(texto, deslocamento):
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

def valida_cpf(cpf_string):
    # TODO: Implementar a lógica
    pass