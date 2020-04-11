miTupla=("a","b","c") #ojo las tuplas se forman con "()"

print(miTupla[:])

#para convertir una tupla en una lista (posible de editar) se usa el METODO "list"
miLista=list(miTupla)
miLista.append("d")
miLista.append("d")

print(miLista)

#para reconvertir la lista en tupla (de vuelta inmodificable) se usa el METODO "tuple"
miTuplaN=tuple(miLista)
print(miTuplaN)
#se identifican las listas y las Tuplas por los "[]" y los "()"

#para comprobar si existe en la tupla un elemento, se usa la INSTRUCCION "in"
print("d" in miTuplaN)

#para averiguar cuantas veces aparece un elemento en la tupla, se usa el METODO "count"
print("Este elemento aparece ", miTuplaN.count("d"), "veces.")

#para averiguar la longitud de la tupla, se el METODO "len"
print("La tupla tiene ", len(miTuplaN), "elementos.")

otraTupla=(19,)#para formar una tupla unitaria
print(otraTupla)


