def hanoi(n, origen, destino, auxiliar):
    global contador
    if n == 1:
        contador += 1
        print(f"Mueve el disco 1 de {origen} a {destino}")
    else:
        hanoi(n-1, origen, auxiliar, destino)
        contador += 1
        print(f"Mueve el disco {n} de {origen} a {destino}")
        hanoi(n-1, auxiliar, destino, origen)

def resolver_hanoi(n, origen, destino):
    global contador
    contador = 0
    print(f"\nPasos para resolver la Torre de Hanoi con {n} discos:")
    hanoi(n, origen, destino, "Auxiliar")
    print(f"\nSe realizaron un total de {contador} movimientos.")

# Solicitar datos al usuario
num_discos = int(input("Ingrese el número de discos: "))
origen = input("Ingrese el lugar donde se encuentra la torre: ")
destino = input("Ingrese el lugar donde quiere mover la torre: ")

# Resolver la Torre de Hanoi
resolver_hanoi(num_discos, origen, destino)