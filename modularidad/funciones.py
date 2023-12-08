
from functools import reduce
from operator import call
from threading import local

from symbol import decorated


def say_hello():
    print('Hello world!')


say_hello()


def one():
    return 1


print(one())

if one() == 1:
    print('One is one!')
else:
    print('One is not one!')


def empty():
    x = 0


print(empty())


def quick():
    return


print(quick())


# Retorno de multiples valores
def multiple():
    return 1, 2, 3  # es una tupla


print(multiple())
print(type(multiple()))

# Podemos aplicar desempaquetado de tuplas
a, b, c = multiple()
print(a, b, c)

# Parametros y argumentos


def sqrt(value):
    return value ** 0.5


print(sqrt(4))


def _min(a, b):
    if a < b:
        return a
    else:
        return b


print(_min(1, 2))
print(_min(6, 2))


def _min(a, b):
    if a < b:
        return a
    return b


print(_min(1, 2))

# Argumentos posicionales


def build_cpu(vendor, num_cores, freq):
    return dict(vendor=vendor, num_cores=num_cores, freq=freq)


print(build_cpu('AMD', 8, 2.7))

# Argumentos nominales
print(build_cpu(freq=2.7, num_cores=8, vendor='AMD'))

# Arguentos posicionales y nominales
print(build_cpu('AMD', 8, freq=2.7))
print(build_cpu('INTEL', num_cores=4, freq=3.1))

# Argumentos mutables e inmutables
values = [2, 3, 4]


def square_it(value):
    for i in range(len(value)):
        value[i] = value[i] ** 2
    return values


print(square_it(values))

# Parametros por defecto


def build_cpu(vendor, num_cores, freq=3.1):
    return dict(vendor=vendor, num_cores=num_cores, freq=freq)


print(build_cpu('INTEL', 4))
print(build_cpu('INTEL', 2, 3.4))

DEFAULT_FREQ = 3.1


def build_cpu(vendor, num_cores, freq=DEFAULT_FREQ):
    return dict(vendor=vendor, num_cores=num_cores, freq=freq)


print(build_cpu('INTEL', 4))


# Modificando parametros mutables
def buggy(arg, result=[]):
    result.append(arg)
    print(result)


buggy(1)
buggy(2, [1, 2, 3, 5])

# Problema de modificacion de parametros mutables


def buggy(arg, result=[]):
    result.append(arg)
    print(result)


buggy(1)
buggy(2)

# Solucion de modificacion de parametros mutables


def works(arg):
    result = []
    result.append(arg)
    return result


print(works(1))
print(works(2))
# La forma de arreglar el código anterior utilizando un parámetro con valor por defecto sería utilizar un tipo de dato inmutable


def nonbuggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)


nonbuggy('a')

nonbuggy('b')

nonbuggy('a', ['x', 'y', 'z'])

nonbuggy('b', ['x', 'y', 'z'])

# Empaquetar/Desempaquetar argumentos
# EMPAQUETAR/DESEMPAQUETAR ARGUMENTOS POSICIONALES
print(sum(4, 3, 2, 1))


def _sum(*values: int) -> int:
    print(f'{values}')
    result = 0
    for value in values:
        result += value
    return result


print(_sum(4, 3, 2, 1))

values = (1, 2, 3, 4)
print(_sum(values))  # Obtenemos un error

# Solucion
values = (1, 2, 3, 4)


def _sum(*values: int) -> int:
    print(f'{values}')
    result = 0
    for value in values:
        result += value
    return result


# Desempaquetar argumentos
print(_sum(*values))

# EMPAQUETAR/DESEMPAQUETAR ARGUMENTOS NOMINALES


def best_student(**marks: int) -> str:
    print(f'{marks=}')
    max_mark = -1
    for student, mark in marks.items():  # marks es un diccionario
        if mark > max_mark:
            max_mark = mark
            best_student = student
    return best_student


print(best_student(ana=8, antonio=6, inma=9, javier=7))

marks = dict(ana=8, antonio=6, inma=9, javier=7)

print(best_student(**marks))

# Convenciones
'''En muchas ocasiones se utiliza args como nombre de parámetro para argumentos posicionales y kwargs como nombre de parámetro para argumentos nominales.'''


def func(*args, **kwargs):
    # TODO
    pass


# Forzando modo de paso de argumentos
# ARGUMENTOS SÓLO NOMINALES
def sum_power(a, b, *, power=False):
    if power:
        a **= 2
        b **= 2
    return a + b


print(sum_power(2, 3, ))
print(sum_power(a=3, b=4))
print(sum_power(3, 4, power=True))
print(sum_power(3, 4, True))

# ARGUMENTOS SÓLO POSICIONALES


def sum_power(a, b, /, power=False):
    if power:
        a **= 2
        b **= 2
    return a + b


print(sum_power(2, 3, ))
print(sum_power(2, 4, True))
print(sum_power(3, 4, power=True))
print(sum_power(a=3, b=4))

# FIJANDO ARGUMENTOS POSICIONALES Y NOMINALES


def sum_power(a, b, /, *, power=False):
    if power:
        a **= 2
        b **= 2
    return a + b


print(sum_power(3, 4, power=True))  # Unico modo de llamarle

# Funciones como parametros


def success():
    print('Success!')


print(type(success()))


def doit(f):
    f()


doit(success)


def repeat_please(text, times=1):
    return text * times


print(type(repeat_please))


def doit(f, arg1, arg2):
    return f(arg1, arg2)


print(doit(repeat_please, 'Hello', 3))

# Documentacion


def sqrt(value):
    'Returns the square root of the value'
    return value ** (1/2)


print(sqrt.__doc__)

# forma ortodoxa


def closest_int(value):
    """Returns the closest integer to the given value.
    The operation is:
        1. Compute distance to floor.
        2. If distance less than a half, return floor.
           Otherwise, return ceil.
    """
    floor = int(value)
    if value - floor < 0.5:
        return floor
    else:
        return floor + 1


print(help(closest_int))
print(closest_int.__doc__)

# Explicacion de parametros
'''Una primera línea de descripción de la función.

A continuación especificamos las características de los parámetros (incluyendo sus tipos).

Por último, indicamos si la función retorna un valor y sus características.'''

# Anotaciones de tipos


def ssplit(text: str, spit_pos: int) -> tuple:
    return text[:spit_pos], text[spit_pos:]


print(ssplit('Always remembre us this way', 15))  # revisar mypy biblioteca

# Volres por defecto


def ssplit(text: str, split_pos: int = -1) -> tuple:
    if split_pos == -1:
        split_pos = len(text) // 2
    return text[:split_pos], text[split_pos:]


print(ssplit('Always remembre us this way'))

# Tipos compuestos
# Anotación        Ejemplo

# list[str]    ['A', 'B', 'C']

# set[int] {4, 3, 9}

# dict[str, float] {'x': 3.786, 'y': 2.198, 'z': 4.954}

# tuple[str, int] ('Hello', 10)

# tuple[float, ...] (1.23, 5.21, 3.62) o (4.31, 6.87) o (7.11,)

# Tipos compuestos
# Anotación        Ejemplo
# tuple|dic        Tupla o diccionario
# list[str|int]     Lista de cadenas de texto o enteros
# set[int|float]    Set de enteros o flotantes

# Numero indefinido de parametros


def _max(*args: int | float):
    pass


# Funciones anonimas
# Funcion lambda
# num_words = lambda t:  len(t.split())
def num_words(t): return len(t.split())


print(type(num_words))
print(num_words)
print(num_words('hola mundo, como es la vida'))


# logic_and = lambda x, y: x & y

# Enfoque funcional
# Map
def f(x):
    return x ** 2 / 2


data = range(1, 11)
map_gen = map(f, data)
print(type(map_gen))
print(list(map_gen))

data = range(1, 11)
print(list(map(lambda x: x**2 / 2, data)))

# Lista por comprension
print([x**2 / 2 for x in data])

# Filter


def odd_number(x):
    return x % 2 == 1


data = range(1, 21)

filter_gen = filter(odd_number, data)
print(type(filter_gen))
print(list(filter_gen))

# usando lambda
data = range(1, 21)
print(list(filter(lambda x: x % 2 == 1, data)))
# usando comprension
print([x for x in data if x % 2 == 1])

# Reduce

# from functools import reduce


def mult_values(x, y):
    return x * y


data = range(1, 6)

print(reduce(mult_values, data))

# Usando lambda
# from functools import reduce

data = range(1, 6)
print(reduce(lambda x, y: x*y, data))

# Generadores
# A diferencia de las funciones ordinarias, los generadores tienen la capacidad de «recordar» su estado para recuperarlo en la siguiente iteración y continuar devolviendo nuevos valores.

# Funciones generadoras
# Los generadores se agotan


def evens(lim: int) -> int:
    for i in range(0, lim + 1, 2):
        yield i


print(type(evens))

evens_gen = evens(20)  # Iterador creado


# Recorrido del iterador
for i in evens_gen:
    print(i, end=' ')

# Expreciones generadoras
# Una expresión generadora es sintácticamente muy similar a una lista por comprensión, pero utilizamos paréntesis en vez de corchetes
evens_gen = (x for x in range(0, 20, 2))
print(evens_gen)
for even in evens_gen:
    print(even, end=' ')

print(sum((x for x in range(0, 20, 2))))
print(min((x for x in range(0, 20, 2))))
print(max((x for x in range(0, 20, 2))))

# Funciones internas
VALID_CHARS = 'xyz'


def validation_rate(text: str) -> float:
    """Rate of valid chars in text."""
    def is_valid_char(char: str) -> bool:
        return char in VALID_CHARS

    cheklist = [is_valid_char(c) for c in text]
    return sum(cheklist) / len(text)


print(validation_rate('zxyzxxyz'))
print(validation_rate('abzxyabcdz'))
print(validation_rate('abc'))

# Clausuras


def make_multiplier_of(n):
    def multipler(x):
        return n * x

    return multipler


m3 = make_multiplier_of(3)
m5 = make_multiplier_of(5)

print(type(m3))
print(type(m5))

print(m3(10))
print(m5(8))

# Decoradores
# Esqueleto basico de un decorador


def my_decorator(func):
    def wrapper(*args, **kwargs):
        # Some code before calling function
        return func(*args, **kwargs)
        # Some code after calling function
    return wrapper


'''
Elemento            Descripción
my_decorator        Nombre del decorador
wrapper             Función interior (convención de nombre)
func                Función a decorar (convención de nombre)
*args               Argumentos posicionales (convención de nombre)
**kwargs            Argumentos nominales (convención de nombre)'''

# Ejemplo


def res2bin(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return bin(result)
    return wrapper


def power(x: int, n: int) -> int:  # Definicion de funcion ordinaria
    return x ** n


print(power(2, 3))

# Aplicamos el decorardor sobre la funcion ordinaria
decorated_power = res2bin(power)
print(decorated_power(2, 3))

# usando @ para decorar


@res2bin
def power(x: int, n: int) -> int:
    return x ** n


print(power(4, 5))

# Manipulando argumentos


def assert_int(func):
    def wrapper(value1: int, value2: int, /) -> int | float | None:
        if isinstance(value1, int) and isinstance(value2, int):
            return func(value1, value2)
        return None
    return wrapper


@assert_int
def _sum(a, b):
    return a + b


result = _sum(2, 3)

print(result)


# Funciones recursivas
def call_me():
    return call_me()


call_me()

# Sucesion de fibonacci


def fibonaci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonaci(n - 1) + fibonaci(n-2)


print(fibonaci(2))
print(fibonaci(3))
print(fibonaci(4))


def get_size(words: list[str]) -> int:
    if len(words) == 0:
        return 0
    return len(words[0]) + get_size(words[1:])


words = ['this', 'is', 'recursive']
print(get_size(words))

# Espacio de nombres
# Acceso a variables globales
lenguage = 'castellano'


def catalonia():
    print(f'{lenguage}')


print(lenguage)
catalonia()


# Creando variables locales
language = 'castellano'


def catalonia():
    language = 'catalan'
    print(f'{language=}')


print(language)
catalonia()
print(language)

# Forzando modificacion global
language = 'castellano'


def catalonia():
    global language
    language = 'catalan'
    print(f'{language=}')


print(language)
catalonia()
print(language)

# Contenido de los espacios de nombres
language = 'castellano'


def catalonia():
    language = 'catalan'
    print(f'{locals()=}')


catalonia()

language = 'castellano'


def catalonia():
    language = 'catalan'
    print(f'{globals()=}')


catalonia()
