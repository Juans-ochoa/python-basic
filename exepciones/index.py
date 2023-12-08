def intdiv(a: int, b: int) -> int:
    try:
        return a//b
    except:
        print('Please do not divide by zero...')


intdiv(5, 0)


def intdiv(a: int, b: int) -> int:
    return a // b


def arithmetics():
    return intdiv(3, 0)


def manage():
    return arithmetics()


def main():
    return manage()


main()


# Ecpecificando excepciones
# TypeError por si los operadores no permiten la division
# ZeroDivisionError por si el denominador es cero.
# Exception para cualquier otro error que se pueda producir.

def intdiv(a: int, b: int) -> int:
    try:
        return a//b
    except TypeError:
        print('Please do not divide by strings...')
    except ZeroDivisionError:
        print('Please do not divide by zero...')
    except Exception:
        print('Something went wrong...')


intdiv(3, '0')

# Agrupando diferentes excepciones


def intdiv(a, b):
    try:
        result = a // b
    except (TypeError, ZeroDivisionError):
        print('Check operands: Some of them caused errors...')
    except Exception:
        print('Ups. Something went wrong...')


intdiv(3, 0)

# Mostrando errores
values = [4, 2, 7]
try:
    print(values[3])
except IndexError as error:
    print(error)

# Elevando excepciones


def _sum(a: int, b: int) -> int:
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    raise TypeError('Operands must be integers!')


print(_sum(4, 3))
print(_sum(4, '3'))
