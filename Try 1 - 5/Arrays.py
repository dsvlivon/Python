"""En Python Array es sinónimo de Lista"""

miLista=["Jon","Jane","Jimmy","Joe","Jack"]
tuLista=["Seymour","Silvia","Saul"]

print(miLista[:])

print(miLista[4])

print(miLista[-2]) #python toma los indices negativos como la inversa. osea cuenta dsd atrás

print(miLista[1:4]) #python permite acceder a una porcion de lista. el indice "A" es inclusivo y el "B" es exclusivo

#para agregar elementos de la lista se usa la instruccion ".append"
miLista.append("Josie") #pero lo agrega al final

#si quiero agregar en algun punto determiando se usa ".insert"
miLista.insert(2,"Jamal")
print(miLista[:])

#y para agregar varios elementos se usa ".extend"
miLista.extend(["Jonny","Jenny","Julia"])#pero tmb van a lo ultimo
print(miLista[:])

index=miLista.index("Jamal")#se usa para determinar el índice de un elemento conocido
print("Jamal es el n°: ", index)

#para comprobr si un elemento se encuentra o no se usa "in"

print ("Jon" in miLista) #devuelve true o falso si esta o no.

#para eliminar un elemento de la lista se usa ".remove"
miLista.remove(miLista[3])
miLista.remove("Jane")
print(miLista[:]) 

#para eliminar el ultima elemento de la lista se usa ".pop"
miLista.pop()#no hace falta darle parametros xq es el ultimo
print(miLista[:]) 

#para concatenar listas se usan simplemente los operadores 
xLista=miLista+tuLista
print(xLista[:])