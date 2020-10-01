#crear ciclo for que permita ingresar 10 numeros contar y mostrar cuantos son pares y cuantos son impares

par=0
impar=0
for x in range(10):
    num=int(input("Digite un numero: "))
    if (num%2==0):
        par=par+1
    else:
        impar=impar+1

print("La cantidad de numeros pares es: " + str(par) + 
"\nLa cantidad de numeros impares es: " + str(impar))