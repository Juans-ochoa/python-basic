temperature = 20
if temperature > 35:
    print('Aviso por alta temperatura')
else:
    print('Parametros normales')

temperature = 28
if temperature < 20:
    if temperature < 10:
        print('Nivel azul')
    else:
        print('Nivel verde')
else:
    if temperature < 30:
        print('Nivel naranja')
    else:
        print('Nivel rojo')

temperature = 28
if temperature < 20:
    if temperature < 10:
        print('Nivel Azul')
    else:
        print('Nivel verde')
elif temperature < 30:
    print('Nivel naranja')
else:
    print('Nivel rojo')

# Asignacion condicionales

temperature = 35

if temperature < 35:
    fire_risk = 'LOW'
else:
    fire_risk = 'HIGH'

print(fire_risk)

temperature = 35
fire_risk = 'LOW' if temperature < 30 else 'HIGH'
print(fire_risk)

# Operadores de comparacion
# Igualdad => ==
# Desigualdad => !=
# Menor que => <
# Menor o igual que => <=
# Mayor que => >
# Mayor o igual que => >=
value = 8
print(value == 8)
print(value != 8)
print(value < 12)
print(value <= 7)
print(value > 4)
print(value >= 9)

x = 15
print(4 <= x <= 12)

# Operadores lógicos
# and | or | not
x = 8
print(x > 4 or x > 12)  # True or False
print(x < 4 or x > 12)  # False or False
print(x > 4 and x > 12)  # True and False
print(x > 4 or x < 12)  # True or True
print(not (x != 8))  # not False

# Valor nulo
value = None
if value:
    print('Value has some useful value')
else:
    print('Value is None, value seems to be void')

value = 99
if value is not None:
    print(f'{value}')

value = None
print(value is None)
print(value == None)
print(id(None))

value = None
print(id(None) == id(value))
print(value is None)


# Veracidad
# cosas» que son evaluadas a False en Python:
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(0.0))
print(bool(''))  # Cadena vacía
print(bool([]))  # Lista vacía
print(bool(()))  # Tupla vacía
print(bool({}))  # Diccionario vacío
print(bool(set()))  # Conjunto vacío

# Veamos algunos objetos que son evaluados en True
print(bool(True))
print(bool('  '))
print(bool(1e-10))
print(bool([0]))
print(bool('🦆'))

# Sentencia match-case

# color = 'red'

# match color:
#     case 'red':
#         print('🔴')
#     case 'green':
#         print('🟢')
#     case 'blue':
#         print('🔵')


# Operador Morsa
# Version tradicional
radius = 4.25
perimeter = 2 * 3.14 * radius

if perimeter < 100:
    print('Increase radius to reach minimum perimeter')
    print('Actual perimeter: ', perimeter)

# Version con operador morsa
radius = 4.25
if (perimeter := 2 * 3.14 * radius) < 100:
    print('Increase radius to reach minimum perimeter')
    print('Actual perimeter: ', perimeter)
