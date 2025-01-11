'''
Escribe una función que recibe cualquier palabra como parametro, y que devuelve todas 
sus letras(sin repetir) en una lista en orden alfabético.
'''

def letras_unicas(palabra):
    mi_set = set()
    for letra in palabra:
        mi_set.add(letra)
    mi_lista = list(mi_set)
    mi_lista.sort()

    return mi_lista

print(letras_unicas('cascarrabias'))