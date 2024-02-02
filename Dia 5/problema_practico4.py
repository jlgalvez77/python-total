'''
Esscribe una funcion llamada contar_primos() que recibe un solo argumento numerico. Esta funcion va a mostrar en pantalla la cantidad de numeros primos que hay entre 0 y el numero que se le ha pasado como argumento.
'''


def contar_primos(num):
    contador = 0
    for n in range(2, num):
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            contador += 1
    print(contador)

