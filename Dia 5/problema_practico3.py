'''
Escribe una funcion que requiera una cantidad indefinida de argumentoos. Lo que hace la 
funcion es devilver True  si en algun momento se ha ingresado el numero 0 repetido 3 veces 
consecutivas. En caso contrario, devolvera False.
'''


def ceros_vecinos(*args):
    contador = 0
    for num in args:
        if contador == len(args):
            return False
        if args[contador] == 0 and args[contador + 1] == 0 and args[contador + 2] == 0:
            return True
        else:
            contador += 1
    return False

print(ceros_vecinos(1, 2, 0, 0, 0, 3, 4, 0, 5))