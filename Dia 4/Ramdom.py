from random import *

aleatorio = randint(1, 50)
print(aleatorio)

aleatorio = round(uniform(1, 5), 1)
print(aleatorio)

aleatorio = random()
print(aleatorio)

colores = ['rojo', 'verde', 'azul', 'amarillo', 'blanco']
color = choice(colores)
print(color)

numeros = list(range(1, 50, 5))
shuffle(numeros)
print(numeros)