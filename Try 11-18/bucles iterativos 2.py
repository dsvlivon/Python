"""
for i in ["UTN","UNLA",3]:
    print("Hola",end="")#es un parametro especial para modificar la salida del print


for i in ["UTN","UNLA",3]:
    print("Hola",end="  ")#se pueden sumar cáracteres para separar

for i in "dsvlivon@gmail.com":
    print("x", end=" ")

flag=False #en python False y True van c la 1er letra Mayuscula
email=input("Introduce tu dirección de email: ")#input hace lo q Prompt en C

for i in email:
    if(i=="@"):
        flag=True

if flag==True: #simplificar con (if flag)
    print("El Email es correcto")
else:
    print("El Email es incorrecto")

"""
email=input("Introduce tu dirección de email: ")#input hace lo q Prompt en C
contadorPunto=0
contadorArroba=0

for i in email:
    if(i=="@"):
        contadorArroba=contadorArroba+1
    if(i=="."):
        contadorPunto=contadorPunto+1


if contadorArroba==1 and contadorPunto==1:
    print("El Email es Correcto") 
else:
    print("El Email es incorrecto") 
    

