'''
Escribe una funcion que requiera una cantidad indefinida de argumentoos. Lo que hace la funcion es devilver True  si en algun momento se ha ingresado el numero 0 repetido 3 veces consecutivas. En caso contrario, devolvera False.
'''


def funcion(*args):
    contador = 0
    for n in args:
        if n == 0:
            contador += 1
            if contador == 3:
                return True
        else:
            contador = 0
    return False
