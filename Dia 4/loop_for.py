lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

for i in lista:
    numero_letra = lista.index(i) + 1
    print(f'Es la letra: {i} que es la número {numero_letra}')


lista_nombres = ['Pablo', 'Laura', 'Fede', 'Luis', 'Julia']

for nombre in lista_nombres:
    if nombre.startswith('L'):
        print(nombre)
    else:
        print('Nombre qué no comienza con L')


numeros = [1, 2, 3, 4, 5]
mi_valor = 0

for numero in numeros:
    mi_valor += numero
print(mi_valor)


palabra = 'Python es genial'

for letra in palabra:
    print(letra)


for l in 'Python':
    print(l)

for objeto in [[1, 2], [3, 4], [5, 6]]:
    print(objeto)

dic = {'k1': 1, 'k2': 2, 'k3': 3}

for item in dic:
    print(item)