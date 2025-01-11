def suma(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(suma(2, 3, 5, 7))