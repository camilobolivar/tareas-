def hanoi(n, origen, destino, libre):
    global contador
    if n == 1:
        contador += 1
        print(f"Mueve el disco 1 de {origen} a {destino}")
    else:
        hanoi(n-1, origen, libre, destino)
        contador += 1
        print(f"Mueve el disco {n} de {origen} a {destino}")
        hanoi(n-1, libre, destino, origen)

def resolver_hanoi(n, origen, destino):
    global contador
    contador = 0
    print(f"\nPasos para resolver la Torre de Hanoi con {n} discos:")
    hanoi(n, origen, destino, "libre")
    print(f"\nSe realizaron un total de {contador} movimientos.")

# Solicitar datos al usuario
num_discos = int(input("Cuantos discos: "))
origen = input("En que pilar se encuentra la torre: ")
destino = input("A donde quiere pasar la torre: ")

print("\nTenga en cuenta que libre es el pilar que sobro\n")

# Resolver la Torre de Hanoi
resolver_hanoi(num_discos, origen, destino)