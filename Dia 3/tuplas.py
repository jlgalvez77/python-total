mi_tupla = (1, 2, 3, 4, 5)
print(type(mi_tupla)) # <class 'tuple'>
print(mi_tupla[1]) # 2
t = (1, 2, 3)
x, y, z = t
print(x, y, z) # 1 2 3

t1 = (1, 2, 3, 1)
print(t1.count(1)) # - Cuenta cuántas veces aparece el valor 1
print(t1.index(3)) # - Devuelve el índice del valor 3