import random

print("BIENVENIDO A PIEDRA, PAPEL Y TIJERAS\nCUAL ES TU NOMBRE\n")
nombre = input()   #solicitamos el nombre del jugador para felicitarlo
print("\nDebes elegir una de las siguientes opciones:\n1. PIEDRA\n2. PAPEL\n3. TIJERAS\nLA SELECCION ES NUMERICA!!!")
op=int(input()) #aqui solicitamos la opcion del jugador
#alertamos al usuario su eleccion
if op == 1:
    print("ELIGIO PIERDA")
if op == 2:
    print("eligio papel")
if op ==3:
    print("ELIGIO TIJERAS")

#vamos a generar la opcion del cpu
cpu=random.randint(1,3)
#alertamos al usuario sobre la eleccion del cpu
print(cpu)
if cpu == 1:
    print("cpu ELIGIO PIERDA")
if cpu == 2:
    print("cpu eligio papel")
if cpu == 3:
    print("cpu ELIGIO TIJERAS")
