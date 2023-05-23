import pandas as pd
import numpy as np

direccion = input("Ingrese la dirección del archivo CSV: ")
df = pd.read_csv(direccion)
print("te mostramos el nombre de las columnas y los datos: ")
print(df.dtypes)

columna_1 = input("Ingrese el nombre de la columna 1: ")
columna_2 = input("Ingrese el nombre de la columna 2: ")
print(df[columna_1].unique())

# Pedir al usuario un valor de la columna 1
valor1 = input("Ingrese el valor de la columna 1: ")

A = df[df[columna_1] != valor1][columna_2]
Y = df[df[columna_1] == valor1][columna_2]

# Calcular el rango de la matriz A
rango_A = np.linalg.matrix_rank(A)

# Verificar si la matriz A es invertible
if rango_A < len(A):
    print("La matriz A no es invertible, hay columnas linealmente dependientes.")
else:
    # Resolver sistema de ecuaciones lineales AX = Y
    X = np.linalg.solve(A, Y)
    # Exportar el resultado a un archivo csv
    np.savetxt(direccion, X, delimiter=',')
