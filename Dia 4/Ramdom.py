from random import *

aleatorio = randint(1, 50) # 1 y 50 son los valores que se pueden generar
print(aleatorio)

aleatorio = round(uniform(1, 5), 1) # 1 y 5 son los valores que se pueden generar
print(aleatorio)

aleatorio = random() # 0 y 1 son los valores que se pueden generar
print(aleatorio)

colores = ['rojo', 'verde', 'azul', 'amarillo', 'blanco'] # Escoge un valor aleatorimante
color = choice(colores)
print(color)

numeros = list(range(1, 50, 5)) # Genera una liste de 1 a 50 con saltos de 5
shuffle(numeros)
print(numeros)