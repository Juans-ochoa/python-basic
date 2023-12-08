sentence = 'Hola, Juanse'
sentence = str.upper(sentence)
print(sentence[-1])
print(sentence[-2])
print(sentence[0])
print(sentence[1])

# Trocear una cadena de texto
poem = '''esto es un poema largo'''
print(poem)

print(str(True))
print(str(10))
print(int('FF', 18))
print('Hola esto es un salto de linea\notra linea\nde nuevo otra linea')
# Tabulador
print('Esto es un tabulador\t40')
print('Comilla simple\'Comillas\'')

# Expresiones literales
texto = r'abc\ndef'
print(texto)


# Leer datos del teclado
name = input('Ingresu su nombre:')
print(name)
print(type(name))

# Repetir cadenas de texto
letter = 'Hola'
print(letter * 5)

# Trocear una cadena
'''
[:]
Extrae la secuencia entera desde el comienzo hasta el final. Es una especia de copia de toda la cadena de texto.

[start:]
Extrae desde start hasta el final de la cadena.

[:end]
Extrae desde el comienzo de la cadena hasta end menos 1.

[start:end]
Extrae desde start hasta end menos 1.

[start:end:step]
Extrae desde start hasta end menos 1 haciendo saltos de tamaño step.
'''
proverb = 'Agua pasada no mueve molino'
print(proverb[:])
print(proverb[12:])
print(proverb[:11])
print(proverb[5:11])
print(proverb[5:11:2])

# Longitud de una cadena
print(len(proverb))

# Pertenencia de un elemento
proverb = 'Más vale malo conocido que bueno por conocer'
print('malo' in proverb)
print('bueno' in proverb)
print('regular' in proverb)

proverb = 'Más vale malo conocido que bueno por conocer'

print(not ('X' in proverb))
print('X' not in proverb)

# Dividir una cadena
proverb = 'No hay mal que por bien no venga'
print(proverb.split())
tools = 'Martillo,Sierra,Destornillador'
print(tools.split(','))

# Particionado
text = '3 + 4'
print(text.partition('+'))

# Limpiar cadenas
serial_number = '\n\t   \n 48374983274832    \n\n\t   \t   \n'
print(serial_number.strip())

# Limpieza por la izquierda
serial_number = '\n\t   \n 48374983274832    \n\n\t   \t   \n'
print(serial_number.lstrip())

# Limpieza por la derecha
serial_number = '\n\t   \n 48374983274832    \n\n\t   \t   \n'
print(serial_number.rstrip())

# Especificar los valores a borrar
serial_number = '\n\t   \n 48374983274832    \n\n\t   \t   \n'
print(serial_number.strip('\n'))

# Realizar busquedas
lyrics = '''Quizás porque mi niñez
Sigue jugando en tu playa
Y escondido tras las cañas
Duerme mi primer amor
Llevo tu luz y tu olor
Por dondequiera que vaya'''

print(lyrics.startswith('Quizás'))
print(lyrics.endswith('Final'))

# Encontrar la primera ocurrencia
print(lyrics.find('amor'))
print(lyrics.index('amor'))

print(lyrics.find('universo'))
print(lyrics.index('universo'))

# Numero de veces que aparece una cadena

lyrics = '''Quizás porque mi niñez
Sigue jugando en tu playa
Y escondido tras las cañas
Duerme mi primer amor
Llevo tu luz y tu olor
Por dondequiera que vaya'''

print(lyrics.count('mi'))
print(lyrics.count('tu'))
print(lyrics.count('él'))

# Reemplazar elementos
proverb = 'Quien mal anda mal acaba'
print(proverb.replace('mal', 'bin'))
print(proverb.replace('mal', 'bin', 1))

# Mayúsculas y minúsculas
proverb = 'quien a buen árbol se arrima Buena Sombra le cobija'

print(proverb.capitalize())
print(proverb.title())
print(proverb.upper())
print(proverb.lower())
print(proverb.swapcase())

# Identificando caracteres
# Detectar si todos los caracteres son letras o números
print('R2D2'.isalnum())
print('C3-PO'.isalnum())
# Detectar si todos los caracteres son números
print('314'.isnumeric())
print('3.14'.isnumeric())
# Detectar si todos los caracteres son letras
print('abc'.isalpha())
print('a-b-c'.isalpha())
# Detectar mayúsculas/minúsculas
print('BIG'.isupper())
print('small'.islower())
print('First Heading'.istitle())

# Interpolación de cadenas
"""Interpolar (en este contexto) significa sustituir una variable por su valor dentro de una cadena de texto."""
name = 'Elon Musk'
age = 49
fortune = 43_300
print(f'Me llamo {name}, tengo {age} años y una fortuna de {fortune} millones')

x = 10
print(f'The varable is {{x={x}}}')

# FORMATEANDO CADENAS
# Dando formato a valores enteros:
mount_height = 3718
print(f'{mount_height:10d}')
print(f'{mount_height:010d}')
# Dando formato a otras bases:
value = 0b10010011
print(f'{value:b}')
value = 0o47622
print(f'{value}')
print(f'{value:o}')
value = 0xab217
print(f'{value}')
print(f'{value:x}')

# Dando formato a valores flotantes:
pi = 3.14159265
print(f'{pi:f}')  # 6 decimales por defecto (se rellenan con ceros si procede)
print(f'{pi:.3f}')
print(f'{pi:12f}')
print(f'{pi:7.2f}')
print(f'{pi:07.2f}')
print(f'{pi:.010f}')
print(f'{pi:e}')

# Alienando valores
text1 = 'how'
text2 = 'are'
text3 = 'you'

print(f'{text1:<7s}|{text2:^11s}|{text3:>7s}')
print(f'{text1:-<7s}|{text2:·^11s}|{text3:->7s}')

'''
Dada la variable:

e = 2.71828
, obtenga los siguientes resultados utilizando «f-strings»:

'2.718'
'2.718280'
'    2.72'  # 4 espacios en blanco
'2.718280e+00'
'00002.7183'
'            2.71828'  # 12 espacios en blanco
'''
e = 2.71828
print(f'{e:.3f}')
print(f'{e:.6f}')
print(f'{e:8.2f}')
print(f'{e:e}')
print(f'{e:010.4f}')
print(f'{e:20f}')

# Caracteres Unicode
rocket_code = '0x1F680'
print(dir(rocket_code))
