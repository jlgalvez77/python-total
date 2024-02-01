if 10 > 9:
    print("10 es mayor que 9")
else:
    print('No es mayor')

mascota = 'perro'

if mascota == 'gato':
    print('Tienes un gato')
elif mascota == 'perro':
    print('Tienes un perro')
else:
    print('Tienes un algo')


edad = 16
calificacion = 8
if edad < 18:
    print('Eres menor de edad')
    if calificacion >= 7:
        print('Aprobado')
    else:
        print('Susspenso')
else:
    print('Eres adulto')