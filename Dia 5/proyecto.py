from random import choice

palabras = ['casa', 'coche', 'perro', 'gato', 'pajaro', 'pescado', 'raton', 'elefante', 'jirafa', 'leon']
palabra_elegida = ''
letras_correctas = []
letras_incorrectas = []
intentos = 6
aciertos = 0
juego_terminado = False

# Elegir palabra
def elegir_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))
    return palabra_elegida, letras_unicas

# Pedir letra
def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'
    while not es_valida:
        letra_elegida = input('Introduce una letra: ').lower()
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print('Por favor, introduce una letra válida')
    return letra_elegida

# Mostrar tablero nuevo
def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta = []
    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('_')
    print(' '.join(lista_oculta))


# Comprobar letra
def comprobar_letra(letra_elegida, palabra_oculta, intentos, coincidencias):
    fin = False
    if letra_elegida in palabra_oculta:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    else:
        letras_incorrectas.append(letra_elegida)
        intentos -= 1
    if intentos == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)
    return intentos, fin, coincidencias

def perder():
    print('Has perdido')
    print(f'La palabra oculta era {palabra}')
    return True


def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print('¡Enhorabuena! Has ganado')


palabra, letras_unicas = elegir_palabra(palabras)

while not juego_terminado:
    print('\n' + '*' * 20 + '\n')
    mostrar_nuevo_tablero(palabra)
    print('\n')
    print(f'Letras incorrectas: {letras_incorrectas}')
    print(f'Letras correctas: {letras_correctas}')
    print(f'Intentos restantes: {intentos}')
    print('\n' + '*' * 20 + '\n')
    letra = pedir_letra()
    intentos, terminado, aciertos = comprobar_letra(letra, palabra, intentos, aciertos)
    juego_terminado = terminado