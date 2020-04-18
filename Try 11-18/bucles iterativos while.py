import math
"""i=1
while i<=10:
    print(f"i vale: {i}")
    i=i+1

print("termino la ejecucion")

answer="y"
while answer=="y":
    answer=input("desea continuar (y/n):)

print("termino la ejecucion")

edad=int(input("Ingrese su edad: ")) #ojo con la instruccion "int" sin eso no funca
while edad<1 or edad>110:
    edad=int(input("Error. Ingrese una edad correcta: "))

print("Su edad es "+ str(edad))"""

print("progama de calculo de raiz cuadrada")
numero=int(input("introduce un numero: "))
intentos=0

while numero<0:
    print("no se puede hallar La raiz de un numero negativo.")
    if intentos==1:
        print("Demasiados intentos. Adios")
        break;
    
    if numero<0:
        intentos=intentos+1
        numero=int(input("introduce un numero: "))

        
solucion=0
if intentos<1:
    #solucion=numero*numero
    solucion=math.sqrt(numero)
    print("La raiz cuadrada de "+str(numero)+" es "+str(solucion))

