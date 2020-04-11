
print("PROGRAMA DE EVALUACION DE NOTAS")

#para introducir un valor por teclado, se usa la ISNTRUCCION "input"
alumno=input("Ingrese su nota: ")


def evaluation(x):
    val="Suspenso"
    if x<4:
        val="Desaprobado"
    elif x>=6:
        val="Promocioando"
    else:
        val="Aprobado con Final"

    return val

print(evaluation(int(alumno)))