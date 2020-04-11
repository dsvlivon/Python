miTupla=["Uruguay","Brasil","Argentina"]
miDiccionario={miTupla[0]:"Montevideo", miTupla[1]:"Sao Paulo", miTupla[2]:"Bs.As"}

print(miDiccionario)

print(miDiccionario["Brasil"])

tupla1=["Jon Doe", 32, 10,3,1988]
tupla2=["Adam Smith", 30, 20,7,1990]
tupla3=["Carl Jhonson", 45, 10,3,1975]
dicPersonas={"employee1":tupla1,"employee2":tupla2,"employee3":tupla3}

print(dicPersonas["employee2"])

print(dicPersonas.keys())
print(dicPersonas.values())
print(len(dicPersonas))