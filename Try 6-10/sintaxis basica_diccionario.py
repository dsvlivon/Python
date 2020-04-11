miDiccionario={"Argentina":"Buenos Aires","Canada":"Otawa","Francia":"Paris"} #ojo las tuplas se forman con "{}"

#para preguntar x un elemento.
print(miDiccionario["Francia"])

#para preguntar x un elemento.
print(miDiccionario)

#para agregar un elemento al diccionario.
miDiccionario["Italia"]="Lisboa"
print(miDiccionario)

#para modificar un elemento del diccionario.
miDiccionario["Italia"]="Roma" #los valores se sobreescriben SIEMPRE ojo, quizás convenga triangular la info
print(miDiccionario)

#para eliminar un elemento del diccionario, se usa el METODO "del"
del miDiccionario["Francia"]
print(miDiccionario)



