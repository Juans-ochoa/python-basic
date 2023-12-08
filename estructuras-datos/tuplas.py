from msvcrt import kbhit


empty_tuple = ()

tenerife_geoloc = (28.46824, -16.25462)

three_wise_men = ('Melchor', 'Gaspar', 'Baltasar')

print(empty_tuple, tenerife_geoloc, three_wise_men)

# Tuplas de un elemento
one_item_tuple = ('Papá Noel')

print(one_item_tuple)
print(type(one_item_tuple))  # str

# Para que sea del tiplo tupla se debe agregar una coma la final
one_item_tuple = ('Papá Noel',)
print(type(one_item_tuple))

# Modificar una tupla
three_wise_men = ('Melchor', 'Gaspar', 'Baltasar')
# three_wise_men[0] = 'Tom Hanks'

# Conversion a otros tipos
shopping = ['Agua', 'Aceite', 'Arroz']
print(tuple(shopping))

# Operaciones con tuplas
'''reverse(), append(), extend(), remove(), clear(), sort()'''

# Desempaquetado de tuplas
three_wise_men = ('Melchor', 'Gaspar', 'Baltasar')
king1, king2, king3 = three_wise_men
print(king1, king2, king3)

# divmod()
quotient, remainder = divmod(7, 3)
print(quotient, remainder)

quotient, remainder = divmod(8, 2)
print(quotient, remainder)


# Intercambio de valores
value1 = 40
value2 = 20

value1, value2 = value2, value1
print(value1, value2)

# Desempaquetado extendido
ranking = ('G', 'A', 'R', 'Y', 'W')
head, *body, tail = ranking

print(head, body, tail)

# Desempaquetado genérico
# Sobre cadenas de texto:
oxygen = 'O2'
first, last = oxygen
print(first, last)

# Sobre listas:
writer1, writer2, writer3 = ['Virginia Woolf', 'Jane Austen', 'Mary Shelley']
print(writer1, writer2, writer3)

text = 'Hello, World!'
word1, word2 = text.split()
print(word1, word2)

# ¿Tuplas por comprensión?
myrange = (number for number in range(1, 6))
print(myrange)
