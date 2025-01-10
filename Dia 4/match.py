# serie = "N-02"

# if serie == "N-01":
#     print("Samsung")
# elif serie == "N-02":
#     print("Apple")
# elif serie == "N-03":
#     print("Huawei")
# else:
#     print("Otra marca")


# match serie:
#     case "N-01":
#         print("Samsung")
#     case "N-02":
#         print("Apple")
#     case "N-03":
#         print("Huawei")
#     case _:
#         print("Otra marca")

cliente = {'nombre': 'Federico',
           'edad': 45,
           'ocupacion': 'Ingeniero',}

pelicula = {'nombre': 'El Padrino',
            'director': 'Francis Ford Coppola',
            'año': 1972,
            'genero': 'Drama',
            'duracion': 175,
            'calificacion': 9.2,
            'recaudacion': 245066411,}

elementos = [cliente, pelicula, 'libro']

for elemento in elementos:
    match elemento:
        case {'nombre': nombre,
              'edad': edad,
              'ocupacion': ocupacion}:
            print('Es un cliente')
            print(nombre, edad, ocupacion)
        case {'nombre': nombre,
              'director': director,
              'calificacion': calificacion}:
            print('Es una pelicula')
            print(nombre, director, calificacion)
        case _:
            print('Es otro tipo de elemento')
            print(elemento)