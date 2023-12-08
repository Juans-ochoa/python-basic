

empty_list = []

languages = ['Python', 'Ruby', 'Javascript']

fibonacci = [0, 1, 1, 2, 3, 5, 8, 13]

data = ['Tenerife', {'cielo': 'limpio', 'temp': 24},
        3718, (28.2933947, -16.5226597)]

saludo = 'Hola este es un saludo'
print(list(saludo))
print(list(range(10)))

shopping = ['Agua', 'Huevos', 'Aceite']
print(shopping[0])
print(shopping[2])
print(shopping[-1])

# Trocear una lista
# [start:end:step]

shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']
print(shopping[0:3])
print(shopping[:3])
print(shopping[2:4])
print(shopping[-1:-4:-1])

shopping = ['Agua', 'Huevos', 'Aceite', 'Sal', 'Limón']

# [::-1] equivale a inveritir la lista
print(shopping[::-1])
# Mediante una funcion reversed()
print(list(reversed(shopping)))


# Agregar al final de una lista
shopping = ['Agua', 'Huevos', 'Aceite']
shopping.append('Atun')
print(shopping)

# Agregar en una posicion especifica
shopping = ['Agua', 'Huevos', 'Aceite']
shopping.insert(1, 'Avena')
print(shopping)
shopping.insert(3, 'Lulo')
print(shopping)

# Repetir elementos
shopping = ['Agua', 'Huevos', 'Aceite']
print(shopping * 3)

# Combinar listas
# Sin modificar la lista original
shopping = ['Agua', 'Huevos', 'Aceite']
fruitshop = ['Lulo', 'Naranja']

print(shopping + fruitshop)

# Modificando la lista original
shopping.extend(fruitshop)
print(shopping)

# Borrar elementos de una lista
# por su indice
shopping = ['Agua', 'Huevos', 'Aceite', 'panela', 'azucar']
del shopping[0]
print(shopping)

# Por su valor
shopping = ['Agua', 'Huevos', 'Aceite', 'panela', 'azucar']
shopping.remove('panela')
print(shopping)

#  Por su indice con extracción
shopping = ['Agua', 'Huevos', 'Aceite', 'panela', 'azucar']

product = shopping.pop(-1)
print(product)
product = shopping.pop(1)
print(product)

# Por su rango
shopping = ['Agua', 'Huevos', 'Aceite', 'panela', 'azucar']
shopping[1:4] = []
print(shopping)

# Borrado completo de la lista
shopping = ['Agua', 'Huevos', 'Aceite', 'panela', 'azucar']
print(id(shopping))
shopping.clear()
print(shopping)
print(id(shopping))


shopping = ['Agua', 'Huevos', 'Aceite', 'panela', 'azucar']
print(id(shopping))
shopping = []
print(shopping)
print(id(shopping))


# Encontrar un elemento
shopping = ['Agua', 'Huevos', 'Aceite', 'panela', 'azucar']
print(shopping.index('Aceite'))
print(shopping.index('Arroz'))

# Pertenencia de un elemento
shopping = ['Agua', 'Huevos', 'Aceite', 'panela', 'azucar']
print('Agua' in shopping)
print('Arroz' in shopping)


sheldon_greeting = ['Penny', 'Penny', 'Penny']
print(sheldon_greeting.count('Howard'))
print(sheldon_greeting.count('Penny'))

# Convertir una lista a cadena de texto
shopping = ['Agua', 'Huevos', 'Aceite', 'panela', 'azucar']
print(','.join(shopping))
print('-'.join(shopping))
print('|'.join(shopping))

date = '12/31/20'
date = date.split('/')

print('-'.join(date))

# Ordenar una lista
# Sin modificar la lista original
shopping = ['Agua', 'Huevos', 'Aceite', 'Panela', 'Azucar']
print(sorted(shopping))

# Modificando la lista original
shopping = ['Agua', 'Huevos', 'Aceite', 'Panela', 'Azucar']
shopping.sort()
print(shopping)

# Ordenamiento en sentido opuesto
shopping = ['Agua', 'Huevos', 'Aceite', 'Panela', 'Azucar']
print(sorted(shopping, reverse=True))

# Modificando la lista original
shopping = ['Agua', 'Huevos', 'Aceite', 'Panela', 'Azucar']
shopping.sort(reverse=True)
print(shopping)

# Iterar usando enumeración
shopping = ['Agua', 'Huevos', 'Aceite', 'Panela', 'Azucar']
for i, product in enumerate(shopping):
    print(i, product)

# Iterar sobre multiples listas - Zip
shopping = ['Agua', 'Huevos', 'Aceite', 'Panela', 'Azucar']
details = ['mineral natural', 'de oliva virgen', 'basmati']

for product, detail in zip(shopping, details):
    print(product, detail)

# Lista explicita
shopping = ['Agua', 'Huevos', 'Aceite', 'Panela', 'Azucar']
details = ['mineral natural', 'de oliva virgen', 'basmati']

print(list(zip(shopping, details)))

v1 = [4, 3, 8, 1]
v2 = [9, 2, 7, 3]
product = 0

for i, j in zip(v1, v2):
    product += i*j
print(f'v1*v2 = {product}')

# Comparar listas
print([1, 2, 3] < [1, 2, 4])

# Cuidado con las copias
original_list = [4, 3, 7, 1]
copy_list = original_list

original_list[0] = 5

print(original_list)
print(copy_list)

# Forma correcta de realizar una copia
original_list = [4, 3, 7, 1]
copy_list = original_list.copy()

original_list[0] = 15

print(original_list)
print(copy_list)

# Realizar copia con troceo, es una aproximacion
original_list = [4, 3, 7, 1]
copy_list = original_list[:]

print(id(original_list) != id(copy_list))

# Veracidad Multiple all
# Versicon clasica
word = 'python'
if len(word) == 4 and word.startswith('p') and word.count('y') >= 1:
    print('Cool word!')
else:
    print('No thanks')

# Version con veracidad multiple
word = 'python'
enought_lenght = len(word) > 4
right_beginning = word.startswith('p')
min_ys = word.count('y') >= 1

is_cool_word = all([enought_lenght, right_beginning, min_ys])

if is_cool_word:
    print('Cool word!')
else:
    print('No thanks')

# Veracidad Multiple any
word = 'yeah'

enough_length = len(word) > 4            # False
right_beginning = word.startswith('p')   # False
min_ys = word.count('y') >= 1  # True

is_fine_word = any([enough_length, right_beginning, min_ys])

if is_fine_word:
    print('Fine word')
else:
    print('No thanks')

# Lista por compresion
# Version clasica
values = '32,45,11,87,20,48'
int_values = []

for value in values.split(','):
    int_values.append(int(value))

print(int_values)

# Lista por compresion
values = '32,45,11,87,20,48'
int_values = [int(value) for value in values.split(',')]
print(int_values)

# Condiciones en comprensiones
values = '32,45,11,87,20,48'
int_values = [int(value)
              for value in values.split(',') if value.startswith('4')]
print(int_values)

# Anidamiento en comprensiones
values = '32,45,11,87,20,48'
svalues = values.split(',')

combinations = [f'{v1}x{v2}' for v1 in svalues for v2 in svalues]
print(combinations)

result_fn = [x * 3 + 2 for x in range(20)]
print(result_fn)

# sys.argv
# import sys
'''Veamos una aplicación de lo anterior en un programa que convierte un número decimal a una determinada base, ambos argumentos pasados por línea de comandos:'''

# number = int(sys.argv[1])
# tobase = int(sys.argv[2])

# match tobase:
#     case 2:
#         result = f'{number: b}'


# Funciones matematicas
# Suma
data = [5, 3, 2, 8, 9, 1]
print(sum(data))

# Min
data = [5, 3, 2, 8, 9, 1]
print(min(data))

# Max
data = [5, 3, 2, 8, 9, 1]
print(max(data))

# Listas de listas
goalkeeper = 'Casillas'
defenders = ['Capdevila', 'Piqué', 'Puyol', 'Ramos']
midfielders = ['Xavi', 'Busquets', 'X. Alonso']
forwards = ['Iniesta', 'Villa', 'Pedro']

team = [goalkeeper, defenders, midfielders, forwards]
print(team)

# Matrices de 2x2
A = [[6, 4], [8, 9]]
B = [[3, 2], [1, 7]]
result = []

for row_a in range(len(A)):
    for row_b in range(len(B)):
        print(f'{A[row_a][row_b]} * {B[row_b][row_a]}-({row_a}, {row_b})')
        product = A[row_a][row_b] * B[row_b][row_a]
        print(product)
