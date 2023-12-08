# While
# want_great = 'S'

# while want_great == 'S':
#     print('Hola que tal!')
#     want_great = input('Quieres continuar? S/N: ')
# print('Que tenga un buen dia!')

# Romper un bucle while
# MAX_GREETS = 4

# greet_count = 0
# want_great = 'S'

# while want_great == 'S':
#     print('Hola que tal!')
#     greet_count += 1

#     if greet_count == MAX_GREETS:
#         print('Máximo número de saludos alcanzado')
#         break

#     want_great = input('Quieres continuar? S/N: ')


# Comprobar a rotura
# MAX_GREETS = 4

# num_greets = 0
# want_great = 'S'

# while want_great == 'S':
#     print('Hola que tal!')
#     num_greets += 1

#     if (num_greets == MAX_GREETS):
#         print('Maximo numero de saludos alcanzado')
#         break
#     want_great = input('Quieres continuar? S/N: ')
# else:
#     print('Usted no quiere mas saludos')

# print('Que tenga un buen dia!')

# Continuar un bucle
# want_great = 'S'
# valid_options = 0

# while want_great == 'S':
#     print('Hola que tal!')
#     want_great = input('Quires otro saludo ? S/N \n')
#     if want_great not in 'SN':
#         print('No le he entendido pero le saludo \n')
#         want_great = 'S'
#         continue
#     valid_options += 1
# print(f'{valid_options} respuestas validas')
# print('Que tenga un buen dia!')

# while True:
#     mark = float(input('Introduzca nueva nota: '))
#     if not (0 <= mark <= 10):
#         print('Nota fuera de rango')
#         break
#     print(mark)


# while 0 <= (mark := float(input('Introduzca una nueva nota: '))) <= 10:
#     print(mark)
# print('Nota fuera de rango')

# Sentencia for
# word = 'Python'

# for letter in word:
#     print(letter)

# # romper el bucle

# word = 'Python'
# for letter in word:
#     if letter == 'h':
#         break
#     print(letter)

# Secuencia de numeros


# for i in range(0, 3):
#     print(i)

# for i in range(3):
#     print(i)

# for i in range(1, 6, 2):
#     print(i)

# for i in range(2, -1, -1):
#     print(i)

# # Usando el gion abajo
# for _ in range(10):
#     print('Repeat me 10 times!')

# # for i in range(0, 101):
# #     print(f'{i}')

# # Bucles anidados
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f'{i} * {j} = {i * j}')

# for i in range(5):
#     for j in range(5):
#         if i == j:
#             symbol = 'X'
#         elif i < j:
#             symbol = 'U'
#         else:
#             symbol = 'D'
#         print(symbol, end=' ')
#     print()

# Ejercicios de repanso
# inputValue = int(input('Introduzca una valor: '))

# accumulator = 0
# sequence = []
# for i in range(inputValue + 1):
#     if accumulator >= inputValue:
#         break
#     if i % 3 == 0:
#         accumulator += i
#         sequence.append(i)
# print(accumulator, sequence)

# cont = 0
# accumulator = 0
# while accumulator <= inputValue:
#     cont += 3
#     accumulator += cont
#     print(f'M: ${cont: 2d} S: {accumulator: 2d}')
# while True:
#     name = input('Introduce tu nombre: ')
#     if not name.istitle():
#         print('Error, debe escribir su nombre correctamente')
#         continue
#     else:
#         print(f'Hola {name}')
#         break

# inputNumber = int(input('Introduce un numero: '))
# product = 1

# for i in range(1, inputNumber + 1):
#     product *= i**2
# print(product)
