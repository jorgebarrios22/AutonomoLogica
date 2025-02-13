import random

print("BIENVENIDO A PIEDRA, PAPEL Y TIJERAS\nCUAL ES TU NOMBRE\n")
nombre = input()   #solicitamos el nombre del jugador para felicitarlo
con = 1

while con==1:

    print("\nDebes elegir una de las siguientes opciones:\n1. PIEDRA\n2. PAPEL\n3. TIJERAS\nLA SELECCION ES NUMERICA!!!")
    op=int(input()) #aqui solicitamos la opcion del jugador

    while op <=0 or op >=4:        #validar el ingreso de la seleccion
        print("ingrese un valor dentro del rango")
        op=int(input())

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
    print("\n \n")

    #validacion por empate, se repetira el codigo hasta que se rompa el empate
    if op == cpu:
        print("HAS EMPATE, JUEGA OTRA PARTIDA PARA DESEMPATAR")
    #si el valor es diferente salimos del bucle   
    elif op != cpu:
        break
        
 #hacemos la comparacion en los casos de ganar       
if (op==1 and cpu ==3)  or (op==2 and cpu==1) or (op==3 and cpu==2):
    print("FELICIDADES "+ nombre + " HAS GANADO")
else: #en los casos restante que perdemos solo enviamos el mensaje
    print("TE HA GANADO LA COMPUTADORA \nSUERTE LA PROXIMA")



    
