from time import time
from hmac import new
import re


class StarWarsDroid:
    pass


c3po = StarWarsDroid()
r2d2 = StarWarsDroid()
bb8 = StarWarsDroid()

print(type(c3po))
print(type(r2d2))
print(type(bb8))

# Agregando metodos


class Droid:
    def switch_on(self):
        print("Switching on")

    def switch_off(self):
        print("Switching off")


k2bo = Droid()

k2bo.switch_on()
k2bo.switch_off()

# Agregando atributos


class Droid:
    def switch_on(self):
        self.on = True
        print("Switching on")

    def switch_off(self):
        self.on = False
        print("Switching off")


k2bo = Droid()
k2bo.switch_on()
print(k2bo.on)
k2bo.switch_off()
print(k2bo.on)

# Incializacion __init__ = constructor


class Droid:
    def __init__(self, name: str):
        self.name = name


droid = Droid("K2BO")

print(droid.name)


# Atributos
# Acceso directo
class Droid:
    def __init__(self, name: str):
        self.name = name


droid = Droid("K2BO")
print(droid.name)

droid.name = "K2BO-2"

print(droid.name)

droid.height = 1.8
print(droid.height)

# Propiedades


class Droid:
    def __init__(self, name: str):
        self.hidden_name = name

    @property
    def name(self) -> str:
        print('Inside the getter')
        return self.hidden_name

    @name.setter
    def name(self, name: str) -> None:
        print('Inside the setter')
        self.hidden_name = name


droid = Droid("K2BO")

print(droid.name)  # Inside the getter

droid.name = "HOLA"  # Inside the setter

print(droid.name)  # Inside the getter

# Valores calculados


class AstromechDroid:
    def __init__(self, name: str, height: float) -> None:
        self.name = name
        self.height = height

    @property
    def periscope_height(self) -> float:
        return 0.3 * self.height


droid = AstromechDroid("R2-D2", 1.05)
print(droid.periscope_height)
droid.periscope_height = 0.4
print(droid.periscope_height)

# Las propiedades no pueden reicibir parametros


class AstromechDroid:
    def __init__(self, name: str, height: float):
        self.name = name
        self.height = height

    @property
    def periscope_height(self, from_ground: bool = False) -> float:
        height_factor = 1.3 if from_ground else 0.3
        return height_factor * self.height


droid = AstromechDroid('R2-D2', 1.05)

print(droid.periscope_height)
# droid.periscope_height = 0.4
droid.periscope_height(from_ground=True)

# Cacheando propiedades


class AstromechDroid:
    def __init__(self, name: str, height: float):
        self.name = name
        self.height = height  # Llamada al setter

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, height: float) -> None:
        self._height = height
        self._periscope_height = None  # Invalidar el cache

    @property
    def periscope_height(self) -> float:
        if self._periscope_height is None:
            print('Calculating periscope height...')
            self._periscope_height = 0.3 * self.height
        return self._periscope_height


droid = AstromechDroid('R2-D2', 1.05)

# Calculating periscope height...
# 0.315
print(droid.periscope_height)
print(droid.periscope_height)  # Cacheado
print('#############################')
droid.height = 1.15
print(droid.periscope_height)
print(droid.periscope_height)  # Cacheado

# Ocultando atributos


class Droid:
    def __init__(self, name: str):
        self.__name = name


droid = Droid('K2BO')
print(droid.__name)  # No es accesible
print(droid._Droid__name)  # Es accesible

# Atributos de la clase


class Droid:
    obeys_owner = True  # Obedece a su dueño


good_droid = Droid()
print(good_droid.obeys_owner)

t1000 = Droid()
t1000.obeys_owner = False
print(t1000.obeys_owner)

print(Droid.obeys_owner)

# Si modificamos un atributo de clase desde un objeto, sólo modificamos el valor en el objeto y no en la clase.

# Si modificamos un atributo de clase desde una clase, modificamos el valor en todos los objetos pasados y futuros.


class Droid:
    obeys_owner = True


droid1 = Droid()
print(droid1.obeys_owner)

droid2 = Droid()
print(droid2.obeys_owner)

Droid.obeys_owner = False  # Cambia pasado y futuro
print(droid1.obeys_owner)
print(droid2.obeys_owner)

# Metodos


class Droid:
    def __init__(self, name: str):
        self.name = name
        self.covered_distance = 0

    def move_up(self, steps: int) -> None:
        self.covered_distance += steps
        print(f'Moved {steps} steps up')


droid = Droid('R2-D2')
droid.move_up(10)
print(droid.covered_distance)
droid.move_up(20)
print(droid.covered_distance)

# Metodo de clase


class Droid:
    count = 0

    def __init__(self):
        Droid.count += 1

    @classmethod
    def total_droids(cls) -> None:
        print(f'{cls.count} droids built so far!')


droid1 = Droid()
droid2 = Droid()
droid3 = Droid()

Droid.total_droids()

# Metodos estaticos


class Droid:
    def __init__(self,):
        pass

    @staticmethod
    def get_droids_categories() -> tuple[str]:
        return ('Messeger', 'Astromech', 'Power', 'Protocol')


print(Droid.get_droids_categories())

# Metodos decorados


class Droid:
    @staticmethod
    def audit(method):
        def wrapper(self, *args, **kwargs):
            print(f'Droid {self.name} running {method.__name__}')
            return method(self, *args, **kwargs)  # Ojo llamada!
        return wrapper

    def __init__(self, name: str):
        self.name = name
        self.pos = [0, 0]

    @audit
    def move(self, x: int, y: int):
        self.pos[0] += x
        self.pos[1] += y

    @audit
    def reset(self):
        self.pos = [0, 0]


droid = Droid('B1')
print(droid.name)

# Metodos magicos
# Los métodos mágicos empiezan y terminan por doble subguión __

# __eq__():

# from __future__ import annotations = se debe de realizar la importacion para utilizar el codigo


class Droid:
    def __init__(self, name: str, serial_number: int):
        self.name = name
        self.serial_number = serial_number

    def __eq__(self, droid: Droid) -> bool:
        return self.name == droid.name


droid1 = Droid('C-3PO', 43974973242)
droid2 = Droid('C-3PO', 85094905984)

print(droid1 == droid2)  # llamada implicita a __eq__
print(droid1.__eq__(droid2))

# Magic methods for comparison
# __eq__ => ==
# __ne__ => !=
# __lt__ => <
# __gt__ => >
# __le__ => <=
# __ge__ => >=

# Magic methods for math
# __add__ => +
# __sub__ => -
# __mul__ => *
# __floordiv__ => //
# __truediv__ => /
# __mod__ => %
# __pow__ => **

# from __future__ import annotations

# Importante Este tipo de operaciones debe devolver un objeto de la clase con la que estamos trabajando.


class Droid:
    def __init__(self, name: str, power: int):
        self.name = name
        self.power = power

    def __add__(self, other: Droid) -> Droid:
        new_name = self.name + '-' + other.name
        new_power = self.power + other.power
        # Hay que devolver un objetode tipo Droid
        return Droid(new_name, new_power)


droid1 = Droid('C3PO', 45)
droid2 = Droid('R2D2', 91)

droid3 = droid1 + droid2

print(f'Fusion droid:\n{droid3.name} with power {droid3.power}')

# sobrecarga de operadores

# from __future__ import annotations


class Droid:
    def __init__(self, name: str, power: int):
        self.name = name
        self.power = power

    def __add__(self, other: Droid | int) -> Droid:
        if isinstance(other, Droid):
            new_name = self.name + '-' + other.name
            new_power = self.power + other.power

        elif isinstance(other, int):
            new_name = self.name
            new_power = self.power + other

        return Droid(new_name, new_power)


droid = Droid('L3-37', 75)
powerful_droid = droid + 25
print(powerful_droid.power)

# Aplicando operador igualdad, comparando objetos de distinta naturaleza
# ¿qué pasaría si comparamos un droide con una cadena de texto?

# from __future__ import annotations


class Droid:
    def __init__(self, name: str, power: int):
        self.name = name
        self.power = power

    def __eq__(self, droid: Droid) -> bool:
        return self.name == droid.name


droid = Droid('C-3PO', 43974973242)

print(droid == 'C-3PO')  # No funciona
'''Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 6, in __eq__
AttributeError: 'str' object has no attribute 'name'''

# from __future__ import annotations


class Droid:
    def __init__(self, name: str, power: int):
        self.name = name
        self.power = power

    def __eq__(self, droid: Droid | object) -> bool:
        if isinstance(droid, Droid):
            return self.name == droid.name
        return False


droid = Droid('C-3PO', 43974973242)
print(droid == 'C-3PO')

# __str__


class Droid:
    def __init__(self, name: str, serial_number: int):
        self.name = name
        self.serial_number = serial_number

    def __str__(self) -> str:
        return f'Droid "{self.name}" serial-no {self.serial_number}'


droid = Droid('R2-D2', 1234)
print(droid)
print(str(droid))
print(f'Droid -> {droid}')

# __REPR__ -> Orientado al desarrollador
'''El método __repr()__ se invoca automáticamente en los dos siguientes escenarios:

Cuando no existe el método __str__() en el objeto y tratamos de encontrar su representación en cadena de texto con str() o print().

Cuando utilizamos el intérprete interactivo de Python y pedimos el «valor» del objeto.'''


class Droid:
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return f"Hi there! I'm {self.name}"


c14 = Droid('C-14')

print(c14)  # __str()__
print(c14.__repr__())  # __repr()__


class Droid:
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return f"Hi there! I'm {self.name}"

    def __repr__(self) -> str:
        return f"[Droid] '{self.name}' @ {hex(id(self))}"


c14 = Droid('C-14')

print(c14)
print(c14.__repr__())

# Gestores de contexto
# Un gestor de contexto permite aplicar una serie de acciones a la entrada y a la salida del bloque de código que engloba.

# __enter__()
# __exit__()


# ejemplo en el que implementamos un gestor de contexto que mide tiempos de ejecución:

# from time import time
class Timer:
    def __enter__(self):
        self.start = time()

    ''' exc_type indicando el tipo de la excepción.
        exc_value indicando el valor (mensaje) de la excepción.
        exc_traceback indicando la «traza» (pila) de llamadas que llevaron hasta la excepción.'''

    def __exit__(self, exc_type, exc_value, exc_traceback):
        # Omit exception handling
        self.end = time()
        exc_time = self.end - self.start
        print(f'Execution time: {exc_time:.5f} seconds')


# usemos nuestro gestor de contexto
with Timer():
    for _ in range(1_000_000):
        x = 2 ** 20

# Crear un contexto para congelar con nuestro ejemplo de los Droids


class Droid:
    def __init__(self, name: str):
        self.name = name
        self.covered_distance = 0

    def move_up(self, steps: int) -> None:
        self.covered_distance += steps
        print(f'Moving {steps} steps')


class FrozenDroid:  # Gestor de contexto!
    def __enter__(self, name: str):
        self.droid = Droid(name)
        return self.droid

    def __exit__(self, *err):
        self.droid.covered_distance = 0


with FrozenDroid() as droid:
    droid.move_up(10)
    droid.move_up(20)
    droid.move_up(30)
    print(droid.covered_distance)
