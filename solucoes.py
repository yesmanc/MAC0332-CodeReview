from collections import Counter

def sao_anagramas(string1, string2):
    if not isinstance(string1, str) or not isinstance(string2, str):
        raise TypeError("As entradas devem ser strings.")

    # padronizacao das strings
    string1 = "".join(filter(str.isalnum, string1)).lower()
    string2 = "".join(filter(str.isalnum, string2)).lower()

    if len(string1) != len(string2):
        return False
    
    # verifica se a quantidade de cada caractere unico (key) das strings eh a mesma
    return Counter(string1) == Counter(string2)

def cifra_de_cesar(texto, deslocamento):
    # TODO: Implementar a lógica
    pass

def valida_cpf(cpf_string):
    # TODO: Implementar a lógica
    pass