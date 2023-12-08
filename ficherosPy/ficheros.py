# Lectura de un fichero
from audioop import add


file = open('./temps.dat', 'r')
print(file)
# leer un fichero
file = open('./temps.dat', 'r')
print(file.read())  # lee todo el fichero
# Devuelve todo el contenido del fichero como una lista (list)
file = open('./temps.dat', 'r')
print(file.readlines())

file = open('./temps.dat', 'r')
print(file.readline())  # lee una linea

# Lectura linea a linea
file = open('./temps.dat', 'r')

for line in file:
    print(line)

# Lectura de las tres primeras lineas, se mueve el puntero de lectura, se desplaza a la siguiente linea del fichero
file = open('./temps.dat', 'r')
for lien in range(3):
    print(file.readline().strip())
print('|-----------------------------------|')
for line in file:
    print(line.strip())

# Los ficheros se agoton
file = open('./temps.dat', 'r')
for line in file:
    print(line.strip(), end=' ')

for line in file:  # No hay salida
    print(line.strip(), end=' ')


# Escritura de un fichero
write_file = open('./write.dat', 'w')
canary_iata = ('TFN', 'TFS', 'LPA', 'GMZ', 'VDE', 'SPC', 'ACE', 'FUE')

for iata in canary_iata:
    write_file.write(iata + '\n')

write_file.close()

# Agregar a un fichero
add_file = open('./write.dat', 'a')
add_file.write('AMS\n')

add_file.close()

# Usando contextos
with open('./temps.dat') as f:
    for line in f:
        min_temp, max_temp = line.strip().split()
        print(f'{min_temp} {max_temp}')
