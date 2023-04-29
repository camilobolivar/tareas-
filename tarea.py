edad = float (input("edad :"))
if edad <0:
    print("no valido")
    edad = float (input("edad :"))
    if edad >0 and edad <17:
        print("usted es menor de edad")
        edad = float (input("edad :"))
        if edad >18:
            print("usted es mayor de edad")
        else: 
            print("Es menor de edad")
    else:
        print("Usted es menor de edad")
else:
    if edad >0 and edad <=18:
        print("usted es menor de edad")
    else:
        print("Es menor de edad")
   


