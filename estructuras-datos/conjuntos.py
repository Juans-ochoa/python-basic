lottery = {21, 10, 46, 29, 31, 94}
print(lottery)
print(type(lottery))

# Forma de crear un conjunto
empty_set = set()
print(empty_set)

print(set('Hi my friend'))
print(set([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]))
print(set(('ADENINA', 'TIMINA', 'TIMINA', 'GUANINA', 'ADENINA', 'CITOSINA')))

# Operacion con conjuntos
# Agregar un elemento
beatles = set(['Lennon', 'McCartney', 'Harrison', 'Starr'])
beatles.add('Best')
print(beatles)

# Eliminar un elemento
beatles = set(['Lennon', 'McCartney', 'Harrison', 'Starr'])
beatles.remove('Lennon')
print(beatles)

# Longitud de un conjunto
beatles = set(['Lennon', 'McCartney', 'Harrison', 'Starr'])
print(len(beatles))

# Iterar sobre un conjunto
beatles = set(['Lennon', 'McCartney', 'Harrison', 'Starr'])
for member in beatles:
    print(member)

# Pertenencia de un elemento a un conjunto
beatles = set(['Lennon', 'McCartney', 'Harrison', 'Starr'])
print('Lennon' in beatles)
print('Mark' in beatles)

# Ordenando conjuntos
marks = {1, 4, 3, 2, 5, 6, 7, 8, 9, 10}
print(sorted(marks))

# Teoria de conjuntos
A = {1, 2}
B = {2, 3}

# Interseccion de conjuntos
print(A & B)
print(A.intersection(B))

# Union de conjuntos
print(A | B)
print(A.union(B))

# Diferencia de conjuntos
print(A - B)
print(A.difference(B))

# Diferencia simetrica de conjuntos
A = {1, 2}
B = {2, 3}
print(A ^ B)
print(A.symmetric_difference(B))

# Inclusion
A = {2, 4, 6, 8, 10}
B = {4, 6, 8}
print(B < A)
print(B <= A)
print(A > B)
print(A >= B)

# Conjuntos por comprensión
m3 = {number for number in range(0, 20) if number % 3 == 0}
print(m3)
