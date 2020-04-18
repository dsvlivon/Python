for i in range(5):
    print(f"el indice es {i}")#es al forma d usar el for c una "variable" de tipo contador, mas similar a C o JS
    #en python la notacion tipo F sirve p concatenar d un texto c el valor d una variable ""


for i in range(1,10,3): 
        print(f"el indice es {i}")
        """el tipo range tambien admite mas parametros a saber:
            1 solo argumento es para repetir x veces el bucle
            2 argumentos son un rango (a,b) siendo (a) inclusivo y (b)exclusivo
            3 argumentos son un rango (a,b,c) siendo (c) el paso. Va d (c) en (c)
        """ 

valido=False
email=input("Introduce tu email: ")
for i in range(len(email)):
    if email[i]=="@":
        valido=True

if valido:
    print("El email es correcto")
else:
    print("El email es incorrecto")