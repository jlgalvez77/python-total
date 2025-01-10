texto = input('Introduce un texto: ').lower()
texto_split = texto.split()
texto_tuple = tuple(texto)

print('Introduce tres letras')
letra1 = input('Primera letra: ').lower()
letra2 = input('Segunda letra: ').lower()
letra3 = input('Tercera letra: ').lower()

print(f'La letra {letra1} aparece {texto_tuple.count(letra1)} veces')
print(f'La letra {letra2} aparece {texto_tuple.count(letra2)} veces')
print(f'La letra {letra3} aparece {texto_tuple.count(letra3)} veces')

print(f'Hay un total de {len(texto_split)} palabras en el texto')

print(f'La primera letra es {texto[0]} y la última es {texto[-1]}')
print(f'El texto invertido es {texto[::-1]}')
if 'python' in texto:
    print('La palabra "python" está en el texto')
else:
    print('La palabra "python" no está en el texto')