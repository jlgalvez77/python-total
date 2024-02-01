palabra = 'python'

lista = [letra for letra in palabra]

print(lista)

lista = [n for n in range(0, 21, 2) if n * 2 > 10]
print(lista)


pies = [10, 20, 30, 40, 50]
metros = [pie * 0.3048 for pie in pies]

print(metros)