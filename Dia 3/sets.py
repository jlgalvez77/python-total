mi_set = set([1, 2, 3, 4, 5])
print(type(mi_set)) # <class 'set'>
print(mi_set) # {1, 2, 3, 4, 5}


otro_set = {1, 2, 3, 4, 5}
print(type(otro_set)) # <class 'set'>
print(otro_set) # {1, 2, 3, 4, 5}

print(len(mi_set)) # 5
print(3 in mi_set) # True

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
print(s3) # {1, 2, 3, 4, 5}

s1.add(4)
s1.remove(2) # Genera error si el elemento no existe
s1.discard(6) # No genera error si el elemento no existe
s1.pop() # Elimina un elemento al azar
s1.clear() # Elimina todos los elementos