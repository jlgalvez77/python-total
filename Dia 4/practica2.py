# // Crea un Loop Whilw que reste de uno en uno los numeros desde el 50 al 0 (ambos ncluidos) con las siguientes condiciones:
# //Si el numero es divisible por 5 mostrar dicho numero en pantalla.
# //Si el numero no es divisible por 5, continuar el loop sin mostrar el valor en pantalla.

numero = 50

while numero >= 0:
    if numero % 5 == 0:
        print(numero)
    numero -= 1

