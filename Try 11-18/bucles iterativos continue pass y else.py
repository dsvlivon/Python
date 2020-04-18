nombre="Daniel Sebastian Vizgarra Livon"
contador=0
espacio=0
for i in nombre:
    if i==" ":
        espacio+=1
        continue
    contador+=1
print("tiene "+str(contador) +" letras en su nombre")
print("con "+str(espacio) +" espacios")


class miClass:
    pass # se usa p q el programa funcione sin romperse y se deja un clase sin definir, para ser definida mas adelante


email=input("introduzca su email:")

for i in email:
    if i=="@":
        arroba=True
    break;
else:
    arroba=False

print(arroba)