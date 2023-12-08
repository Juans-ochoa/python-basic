class Droid:
    '''Clase Base'''
    pass


class ProtocolDroid(Droid):
    '''Clase Derivada'''
    pass


print(issubclass(ProtocolDroid, Droid))  # Comprobacion de herencia


class Droid:
    def switch_on(self):
        print('Hi!, I am a droid. Can I help you?')

    def switch_of(self):
        print('Bye! I am going to sleep')


class ProtocolDroid(Droid):
    pass


r2d2 = Droid()
c3po = ProtocolDroid()

r2d2.switch_on()
c3po.switch_on()  # Methodo heredado de la clase Droid

r2d2.switch_of()
c3po.switch_of()

# Sobreescribir un metodo


class Droid:
    def switch_on(self):
        print('Hi!, I am a droid. Can I help you?')

    def switch_of(self):
        print('Bye! I am going to sleep')


class ProtocolDroid(Droid):
    def switch_on(self):
        print('Hi!, I am a protocol droid. Can I help you?')


r2d2 = Droid()
c3po = ProtocolDroid()

r2d2.switch_on()
c3po.switch_on()  # Metodo heredado pero sobreescrito en la clase ProtocolDroid

# Agregar un metodo


class Droid:
    def switch_on(self):
        print('Hi!, I am a droid. Can I help you?')

    def switch_of(self):
        print('Bye! I am going to sleep')


class ProtocolDroid(Droid):
    def switch_on(self):
        print('Hi!, I am a protocol droid. Can I help you?')

    def translate(self, msg: str, from_lang: str) -> str:
        """Translate from language to Human understanding"""
        return f'{msg} means "ZASCA" in {from_lang}'


r2d2 = Droid()
c3po = ProtocolDroid()

print(c3po.translate('Kiitos', from_lang='Huttese'))  # Idioma de Watoo
# Droid generico no puede traducir
r2d2.translate('Kiitos', from_lang='Huttese')

# Accediendo a la clase base


class Droid:
    def __init__(self, name: str):
        self.name = name


class ProtocolDroid(Droid):
    def __init__(self, name: str, languages: list[str]):
        super().__init__(name)  # Llama al constructor de la clase base
        self.languages = languages


droid = ProtocolDroid('C-3PO', ['Ewokese', 'Huttese', 'Jawaese'])
print(droid.name)  # Fijado en el constructor de la clase base
print(droid.languages)  # Fijado en el constructor de la clase derivada

# Herencia multiple


class Droid:
    def greet(self):
        return "Hi, I'm a droid"


class ProtocolDroid(Droid):
    def greet(self):
        return "Hi, I'm a protocol droid"


class AstromechDroid(Droid):
    def greet(self):
        return "Hi, I'm a astromech droid"


class SuperDroid(ProtocolDroid, AstromechDroid):
    pass


class HyperDroid(AstromechDroid, ProtocolDroid):
    pass


print(issubclass(SuperDroid, (AstromechDroid, ProtocolDroid, Droid)))
print(issubclass(HyperDroid, (AstromechDroid, ProtocolDroid, Droid)))

super_droid = SuperDroid()
hyper_droid = HyperDroid()

print(super_droid.greet())
print(hyper_droid.greet())

PY_TYPES = (int, str, float, tuple, list, bool)
print(all(issubclass(_type, object) for _type in PY_TYPES))

# Mixins


class Introspection:
    def dig(self):
        print(vars(self))  # vars devuelve las variables del argumento


class Droid(Introspection):
    pass


droid = Droid()
droid.code = 'K2BO'
droid.num_feet = 2
droid.type = 'Power droid'

droid.dig()

# agregacion y composicion
# Agregacion


class Tool:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name.upper()


class Droid:
    def __init__(self, name: str, serial_number: int, tool: Tool):
        self.name = name
        self.serial_number = serial_number
        self.tool = tool  # Agregacion

    def __str__(self):
        return f'Droid {self.name} armed with a {self.tool}'


lighter = Tool('lighter')
bb8 = Droid('BB-8', 1234, lighter)

print(bb8)

# Estructuras magicas
# Secuencias
'''Una secuencia en Python es un objeto en el que podemos acceder a cada uno de sus elementos a través de un índice, así como calcular su longitud total.'''


class Droid:
    def __init__(self, name: str, parts: list[str]):
        self.name = name
        self.parts = parts

    def __setitem__(self, index: int, part: str) -> None:
        self.parts[index] = part

    def __getitem__(self, index: int) -> str:
        return self.parts[index]

    def __len__(self):
        return len(self.parts)


droid = Droid('R2-D2', ['Radar Eye', 'Pocket Vent', 'Battery Box'])

print(droid.parts)
print(droid[0])  # __getitem__(0)
print(droid[1])  # __getitem__(1)

droid[1] = 'Holographic Projector'  # __setitem__()

print(droid.parts)
print(len(droid))  # __len__()


# Diccionarios
class Droid:
    def __init__(self, name: str, parts: dict[str, float]):
        self.name = name
        self.parts = parts

    def __setitem__(self, part: str, version: float) -> None:
        self.parts[part] = version

    def __getitem__(self, part: str) -> float:
        return self.parts.get(part)

    def __len__(self):
        return len(self.parts)


droid = Droid(
    'R2-D2',
    {
        'Radar Eye': 1.1,
        'Pocket Vent': 3.0,
        'Battery Box': 2.8
    }
)

print(droid.parts)
print(droid['Radar Eye'])
print(droid['Pocket Vent'])
print(droid['Battery Box'])

droid['Battery Box'] = 2.9

print(droid.parts)

print(len(droid))

# Iterables


class Droid:
    def __init__(self, serial: str):
        self.serial = serial * 5

    def __str__(self):
        return f'Droid SN={self.serial}'


class Geonosis:
    def __init__(self, num_droids: int):
        self.num_droids = num_droids
        self.pointer = 0

    def __iter__(self):
        # El iterador es el propio objeto!
        return self

    def __next__(self):
        # Protocolo de iteracion
        if self.pointer >= self.num_droids:
            raise StopIteration
        droid = Droid(str(self.pointer))
        self.pointer += 1
        return droid


for droid in Geonosis(10):
    print(droid)

# Iterables desde afuera
# Enumeracion
tool = enumerate([1, 2, 3])
print(iter(tool) is not None)  # es iterable
print(iter(tool) is tool)  # es su propio iterador
print(next(tool))
print(next(tool))
print(next(tool))

# Rangos
tool = range(1, 4)
print(iter(tool) is not None)  # es iterable
print(iter(tool) is tool)  # usa otro iterador

tool_iterator = iter(tool)
print(tool_iterator)
print(next(tool_iterator))
print(next(tool_iterator))
print(next(tool_iterator))

# Invertido
tool = reversed([1, 2, 3])
print(iter(tool) is not None)  # es iterable
print(iter(tool) is tool)  # es su propio iterador
print(next(tool))
print(next(tool))
print(next(tool))

# Comprimir
tool = zip([1, 2], [3, 4])
print(iter(tool) is not None)  # es iterable)
print(iter(tool) == tool)  # usa otro iterador
print(next(tool))
print(next(tool))


# Estructura de una clase
class OrganizedClass:
    '''Descripcion'''

    # Constructor

    # Metodos de instancia

    # Propiedades

    # Metodos magicos

    # Decoradores

    # Metodos de clase

    # Metodos estaticos
