import os

def Temperaturas():
    print ("--- Opcion de temperaturas ---")
    veces=int(input("Cuantas temperaturas ingresa): "))
    suma=0
    for x in range(veces):
        tempe=float(input("Ingrese temperatura: "))
        suma=suma+tempe
    print("El promedio de las temperaturas es: ", round((suma/veces),2))
    tecla=input("Presione una tecla para continuar")

def personas():
    print("--- Opción de Datos de Personas ---")
    #ingresar para n personas el nombre y la edad. n debe ser ingresado por teclado
    #mostrar: cuantas personas son mayores de edad y cuantas son menores de edad.
    #subir un tercer commit a git con el mensaje "se agrego la opcion dos al menú"
    
    mayores = 0
    menores = 0
    x = 1
    n=int (input("Cuantas personas desea ingresar?: "))
    while (x<=n):        
        input("Nombre de la persona?: ")
        edad=int (input("Que Edad tiene?: "))
        if(edad <= 18):
            mayores = mayores + 1
        else:
            menores = menores + 1
        x = x + 1
    print("Cantidad de Mayores de edad: " + str(mayores))
    print("Cantidad de Manosres de edad: " + str(menores))
    tecla=input("Presione una tecla para continuar")

seguir = True
while seguir:
    os.system('cls')
    print ("1. Temperaturas")
    print ("2. Datos de personas")
    print ("3. SALIR")
    op=int(input("Ingrese opción 1,2,3: "))
    if(op==1):
        Temperaturas()
    if(op==2):
        personas()
    if(op==3):
        print("Programa Finalizado")
        break


    
