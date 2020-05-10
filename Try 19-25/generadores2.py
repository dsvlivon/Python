"""
Se crea una función básica que construya una lista de 
números pares y devuelva esa lista
"""
"""
def  generaPares(limite):
    num=1
    miLista=[]
   
    while num<limite:
        miLista.append(num*2)
        num=num+1

    return miLista

print(generaPares(10))
"""

def  generaPares(limite):
    num=1
    
    while num<limite:
        yield num*2
        num=num+1
    
devuelvePares=generaPares(10)
"""for i in devuelvePares:
   print(i) //esto usaria si quisiera imprimir todos los objetos"""

"""y esto para devolver de a uno y enviar la función a standBy"""
print(next(devuelvePares))
print("Aquí podría ir mas codigo... ") 

print(next(devuelvePares))
print("Aquí podría ir mas codigo... ")

print(next(devuelvePares))
print("Aquí podría ir mas codigo... ")
