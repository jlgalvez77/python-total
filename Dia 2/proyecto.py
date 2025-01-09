name = input('Cual es tu nombre? ')
sales = float(input('Cual es el total de ventas? '))
commission = sales * 13 / 100
print(f'Hola {name}, tu comisión es de {round(commission, 2)}')