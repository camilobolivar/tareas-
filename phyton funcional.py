# 1. Triplicar los números en una lista
lista_enteros = [2, 4, 6, 8, 10]
lista_triplicada = list(map(lambda x: x * 3, lista_enteros))
print("Lista original:", lista_enteros)
print("Lista triplicada:", lista_triplicada)

# 2. Agregar tres listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [7, 8, 9]
resultado = list(map(lambda x, y, z: x + y + z, lista1, lista2, lista3))
print(resultado)

# 3. Imprimir cadenas de una lista individualmente
lista = ['manzana', 'naranja', 'plátano']
list(map(lambda x: print(x), lista))

# 4. Crear lista de potencias
base = 2
exponentes = [0, 1, 2, 3, 4]
resultado = list(map(lambda x: base ** x, exponentes))
print(resultado)

# 5. Cuadrar los elementos de una lista
numeros = [3, 5, 6, 8, 10]
cuadrados = list(map(lambda x: x ** 2, numeros))
print(cuadrados)

# 6. Convertir caracteres a mayúsculas y minúsculas, y eliminar duplicados
secuencia = "Reducir una secuencia de caracteres"
mayusculas = secuencia.upper()
minusculas = secuencia.lower()
sin_duplicados = "".join(set(secuencia))
print("Secuencia original:", secuencia)
print("Secuencia en mayúsculas:", mayusculas)
print("Secuencia en minúsculas:", minusculas)
print("Secuencia sin letras duplicadas:", sin_duplicados)

# 7. Sumar y restar dos listas
from functools import reduce
lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]
suma = list(map(lambda x, y: x + y, lista1, lista2))
resta = list(map(lambda x, y: x - y, lista1, lista2))
diferencia = reduce(lambda x, y: x + y, resta)
print(f'La suma es {suma}')
print(f'La resta es {resta}')
print(f'La diferencia es {diferencia}')

# 8. Convertir lista de enteros y tupla a lista de cadenas
lista = [1, 2, 3]
tupla = (4, 5, 6)
resultado = list(map(lambda x: str(x), lista + list(tupla)))
print(resultado)

# 9. Tomar elementos de una tupla y convertir a enteros
tupla = ('12', '34', '56', '78')
indices = (0, 2, 3)
numeros_enteros = list(map(lambda i: int(tupla[i]), indices))
print(numeros_enteros)

from functools import reduce

# 10. Calcular el cuadrado de los primeros N números de Fibonacci
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib

n = int(input("Ingrese el valor de N: "))
fibonacci_secuencia = fibonacci(n)
fibonacci_cuadrados = list(map(lambda x: x**2, fibonacci_secuencia))
fibonacci_cuadrados_lista = reduce(lambda x, y: x + [y], fibonacci_cuadrados, [])
print(f"Los primeros {n} números de Fibonacci elevados al cuadrado son: {fibonacci_cuadrados_lista}")

# 11. Calcular la suma de los elementos de una matriz de enteros
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
suma = reduce(lambda x, y: x + y, [reduce(lambda x, y: x + y, fila) for fila in matriz])
print(suma)

# 12. Encontrar la razón de números positivos, negativos y ceros en una matriz de enteros
numeros = [1, -2, 0, 3, -4, 5, 0, -6, 7, 8, -9]
positivos = list(filter(lambda x: x > 0, numeros))
negativos = list(filter(lambda x: x < 0, numeros))
ceros = list(filter(lambda x: x == 0, numeros))
razon_positivos = len(positivos) / len(numeros)
razon_negativos = len(negativos) / len(numeros)
razon_ceros = len(ceros) / len(numeros)
print(f"Razón de números positivos: {razon_positivos:.2f}")
print(f"Razón de números negativos: {razon_negativos:.2f}")
print(f"Razón de ceros: {razon_ceros:.2f}")

# 13. Intercalar dos listas en otra lista al azar
import random
import itertools

lista1 = [1, 3, 5, 7, 9]
lista2 = [2, 4, 6, 8, 10]
intercalados = list(itertools.chain(*zip(lista1, lista2)))
random.shuffle(intercalados)
print(intercalados)

# 14. Dividir un diccionario dado de listas en una lista de diccionarios utilizando la función map
diccionario = {
    'frutas': ['manzana', 'pera', 'plátano'],
    'verduras': ['zanahoria', 'lechuga', 'tomate'],
    'bebidas': ['agua', 'refresco', 'cerveza']
}
lista_diccionarios = list(map(lambda x: {k: v[x] for k, v in diccionario.items()}, range(len(next(iter(diccionario.values()))))))
print(lista_diccionarios)

# 15. Escribir un programa en Python para convertir una lista dada de cadenas en una lista de listas usando la función map:
strings = ['hola', 'mundo', 'programacion', 'funcional']
listas = list(map(lambda s: list(s), strings))
listas_de_una_cadena = list(map(lambda l: ''.join(l), listas))
print(listas_de_una_cadena)

# 16. Escribir un programa en Python para convertir una lista dada de tuplas en una lista de cadenas usando la función map:
lista_tuplas = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
lista_cadenas = list(map(lambda tupla: ''.join(map(str, tupla)), lista_tuplas))
print(lista_cadenas)