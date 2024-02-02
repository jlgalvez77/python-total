precios_cafe = [('capuccino', 3.5), ('latte', 4), ('espresso', 2.5), ('americano', 2)]

for elemento in precios_cafe:
    print(f'El precio del {elemento[0]} es de {elemento[1]} euros')

def cafe_mas_caro(lista_precios):
    precio_mayor = 0
    cafe_mas_caro = ''

    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass


    return (cafe_mas_caro, precio_mayor)

print(cafe_mas_caro(precios_cafe))
print(f'El café más caro es el {cafe_mas_caro(precios_cafe)[0]} y cuesta {cafe_mas_caro(precios_cafe)[1]} euros')