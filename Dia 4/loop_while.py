# monedas = 5

# while monedas > 0:
#     print(f'Tengo {monedas} monedas')
#     monedas -= 1
# else:
#     print('No tengo más monedas')


# repuesta = 's'

# while repuesta == 's':
#     respuesta = input('Quieres seguir jugando? s/n: ')
# else:
#     print('Adios')

nombre = input('Ingresa tu nombre: ')

for letra in nombre:
    if letra == 'a':
        break
    print(letra)