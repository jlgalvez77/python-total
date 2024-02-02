'''
Escribe una función que recibe cualquier palabra como parametro, y que devuelve todas sus letras(sin repetir) en una lista en orden alfabético.
'''

def palabras(*args):
    lista = []
    for palabra in args:
        lista.append(sorted(set(palabra)))
    return lista

    