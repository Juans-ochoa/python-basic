# Creando un diccionario
from statistics import mean


empty_dict = {}
print(empty_dict)
print(type(empty_dict))

rae = {
    'bifronte': 'De dos frentes o dos caras',
    'anarcoide': 'Que tiende al desorden',
    'montuvio': 'Campesino de la costa'
}

print(rae)

population_can = {
    2015: 2_135_209,
    2016: 2_154_924,
    2017: 2_177_048,
    2018: 2_206_901,
    2019: 2_220_270
}

print(population_can)

# Conversion
listaToDict = dict(['a1', 'b2'])
print(listaToDict)

# Diccionario a partir de una tupla de cadenas de texto
print(dict(('a1', 'b2')))

# Diccionario a partir de una lista de listas
print(dict([['a', 1], ['b', 2]]))

# Diccionario asignado un valor a cada llave
print(dict.fromkeys('asdf', 1))

# Operaciones con diccionarios
rae = {
    'bifronte': 'De dos frentes o dos caras',
    'anarcoide': 'Que tiende al desorden',
    'montuvio': 'Campesino de la costa'
}

# Obtener un valor
print(rae['bifronte'])

# Obtener un valor usando GET
rae = {
    'bifronte': 'De dos frentes o dos caras',
    'anarcoide': 'Que tiende al desorden',
    'montuvio': 'Campesino de la costa'
}
print(rae.get('bifronte'))
print(rae.get('none', 'No hay resultados'))

# Agregar o modificar un valor
rae = {
    'bifronte': 'De dos frentes o dos caras',
    'anarcoide': 'Que tiende al desorden',
    'montuvio': 'Campesino de la costa'
}
rae['enjuiciar'] = 'Someter una cuestión a examen, discusión y juicio'

print(rae)

rae['enjuiciar'] = 'Instruir, juzgar o sentenciar una causa'
print(rae)

# CREANDO DESDE VACÍO
VOWELS = 'aeiou'
enum_vowels = {}
for i, vowel in enumerate(VOWELS, start=1):
    enum_vowels[vowel] = i

print(enum_vowels)

# Pertenecia de una clave
rae = {
    'bifronte': 'De dos frentes o dos caras',
    'anarcoide': 'Que tiende al desorden',
    'montuvio': 'Campesino de la costa'
}
print('bifronte' in rae)
print('hola' in rae)
print('montuvio' in rae)

# Obtener todos los elementos
rae = {
    'bifronte': 'De dos frentes o dos caras',
    'anarcoide': 'Que tiende al desorden',
    'montuvio': 'Campesino de la costa'
}
# Obtener las llaves de un diccionario
print(rae.keys())
# Obtener los valores de un diccionario
print(rae.values())
# Obtener toodos los pares clave-valor del diccionario
print(rae.items())

# Longitud de un diccionario
rae = {
    'bifronte': 'De dos frentes o dos caras',
    'anarcoide': 'Que tiende al desorden',
    'montuvio': 'Campesino de la costa'
}
print(len(rae))

# Iterar sobre un diccionario
# iterar sobre claves
rae = {
    'bifronte': 'De dos frentes o dos caras',
    'anarcoide': 'Que tiende al desorden',
    'montuvio': 'Campesino de la costa'
}
for word in rae.keys():
    print(word)

# iterar sobre valores
for value in rae.values():
    print(value)

# Iterar sobre clave valor
for word, meaning in rae.items():
    print(f'{word}: {meaning}')

# Combinar diccionarios
rae1 = {
    'bifronte': 'De dos frentes o dos caras',
    'enjuiciar': 'Someter una cuestión a examen, discusión y juicio'
}

rae2 = {
    'anarcoide': 'Que tiende al desorden',
    'montuvio': 'Campesino de la costa',
    'enjuiciar': 'Instruir, juzgar o sentenciar una causa'
}

# Sin modificar los diccionarios originales
print({**rae1, **rae2})
print(rae1 | rae2)

# Modificando los diccionarios originales
rae1 = {
    'bifronte': 'De dos frentes o dos caras',
    'enjuiciar': 'Someter una cuestión a examen, discusión y juicio'
}

rae2 = {
    'anarcoide': 'Que tiende al desorden',
    'montuvio': 'Campesino de la costa',
    'enjuiciar': 'Instruir, juzgar o sentenciar una causa'
}
rae1.update(rae2)
print(rae1)

# Borrar un elemento
rae = {
    'bifronte': 'De dos frentes o dos caras',
    'anarcoide': 'Que tiende al desorden',
    'montuvio': 'Campesino de la costa'
}

# Por su clave
del rae['bifronte']
# Por su clave (con extraccion)
rae.pop('anarcoide')

print(rae)
# Borrar todos los elementos
rae = {
    'bifronte': 'De dos frentes o dos caras',
    'anarcoide': 'Que tiende al desorden',
    'montuvio': 'Campesino de la costa'
}
rae.clear()
print(rae)
# Reiniciando el valor del diccionario
rae = {
    'bifronte': 'De dos frentes o dos caras',
    'anarcoide': 'Que tiende al desorden',
    'montuvio': 'Campesino de la costa'
}

rae = {}
print(rae)

# Cuidado con las copias
original_rae = {
    'bifronte': 'De dos frentes o dos caras',
    'anarcoide': 'Que tiende al desorden',
    'montuvio': 'Campesino de la costa'
}

copy_rae = original_rae
original_rae['bifronte'] = 'La la lala la'
print(copy_rae)

# Posible solucion
original_rae = {
    'bifronte': 'De dos frentes o dos caras',
    'anarcoide': 'Que tiende al desorden',
    'montuvio': 'Campesino de la costa'
}
copy_rae = original_rae.copy()
original_rae['bifronte'] = 'La la lala la'
print(copy_rae)

# Diccionarios por compresion
words = ('sun', 'space', 'rocket', 'earth')
words_length = {word: len(word) for word in words}
print(words_length)

words = ('sun', 'space', 'rocket', 'earth')
words_length = {w: len(w) for w in words if w[0] not in 'aeiou'}
print(words_length)
