def suma(**kwargs):
    total = 0
    for clave, valor in kwargs.items():
        print(f'{clave} -> {valor}')
        total += valor
    return total

print(suma(a=1, b=2, c=3))


def prueba(num1, num2, *args, **kwargs):
    print(f'El primer número es {num1}')
    print(f'El segundo número es {num2}')
    for arg in args:
        print(f'Argumento extra: {arg}')
    for clave, valor in kwargs.items():
        print(f'{clave} -> {valor}')

prueba(1, 2, 3, 4, 5, a=6, b=7, c=8)