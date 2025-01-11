# def chequear_3_cifras(numero):
#     return numero in range(100, 1000)

# suma = 586 + 402

# resultado = chequear_3_cifras(suma)
# print(resultado)

# def chequear_3_cifras(lista):
#     for n in lista:
#         if n in range(100, 1000):
#             return True
#         else:
#             pass
#     return False

# resultado = chequear_3_cifras([55, 99, 600])
# print(resultado)


def chequear_3_cifras(lista):
    lista_3_cifras = []
    for n in lista:
        if n in range(100, 1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras

resultado = chequear_3_cifras([555, 99, 600])
print(resultado)