import os

def Temperaturas():
    print ("--- Opcion de temperaturas ---")
    veces=int(input("Cuantas temperaturas ingresa): "))
    suma=0
    for x in range(veces):
        tempe=float(input("Ingrese temperatura: "))
        suma=suma+tempe
    print("El promedio de las temperaturas es: ", round((suma/veces),2))
    tecla=input("presione una tecla para continuar")

def personas():
    print("--- Opción de Datos de Personas ---")

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


    
