from random import *

intentos = 0
nombre= input('¿Cuál es tu nombre? ')
print(f'Hola {nombre}, vamos a jugar a adivinar un número entre 1 y 100')
print('Tienes 8 intentos')

numero_aleatorio = randint(1, 100)

while intentos < 8:
    numero = int(input('Di un número: '))
    intentos += 1
    if numero < 1 or numero > 100:
        print('El número debe estar entre 1 y 100')
    elif numero < numero_aleatorio:
        print('El número es mayor')
    elif numero > numero_aleatorio :
        print('El número es menor')
    else:
        print(f'¡Felicidades {nombre}! Has adivinado el número en {intentos} intentos')
        break
    
if numero != numero_aleatorio:
    print(f'Lo siento {nombre}, has perdido. El número era {numero_aleatorio}')

