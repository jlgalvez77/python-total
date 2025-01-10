diccionario = {'c1': 'valor1', 'c2': 'valor2'}
print(type(diccionario)) # <class 'dict'>
print(diccionario) # {'c1': 'valor1', 'c2': 'valor2'}

resultado = diccionario['c1'] # 'valor1'
print(resultado)

cliente = {'nombre': 'Juan', 'apellido': 'Perez', 'edad': 30, 'peso': 70.5}
consulta = cliente['nombre']
print(consulta) # Juan

dic = {'c1': 55, 'c2': [10, 20, 30], 'c3': {'s1': 100, 's2': 200}}
print(dic['c2'][1]) # 20
print(dic['c3']['s2']) # 200

dic2 = {'c1': ['a','b','c'], 'c2': ['d','e','f']}
print(dic2['c2'][1].upper()) # E

dic3 = {1: 'a', 2: 'b'}
print(dic) # {1: 'a', 2: 'b'}
dic3[3] = 'c'
print(dic3) # {1: 'a', 2: 'b', 3: 'c'}
dic3[2] = 'B'
print(dic3) # {1: 'a', 2: 'B', 3: 'c'}

print(dic3.keys()) # dict_keys([1, 2, 3])
print(dic3.values()) # dict_values(['a', 'B', 'c'])
print(dic3.items()) # dict_items([(1, 'a'), (2, 'B'), (3, 'c')])