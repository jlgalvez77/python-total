mi_lista = ['a', 'b', 'c']
otra_lista = [True, 50, 'hola', 5.5]
print(type(mi_lista)) # <class 'list'>
resultado = len(mi_lista)
print(resultado) # 3
resultado = len(otra_lista) # 4
print(mi_lista + otra_lista)
otra_lista[0] = 'A' # Cambia el primer elemento
otra_lista.append('Nuevo') # Añade un elemento al final
otra_lista.pop() # Elimina el último elemento

eliminado = otra_lista.pop(1) # Elimina el segundo elemento y lo guarda en una variable
print(eliminado) # 50

lista = ['g', 'o', 'b', 'm', 'c']
lista.sort() # Ordena la lista
print(lista) # ['b', 'c', 'g', 'm', 'o']
lista.reverse() # Invierte la lista
print(lista) # ['o', 'm', 'g', 'c', 'b']