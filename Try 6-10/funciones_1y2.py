
numA=4
numB=7

msg1="el primer numero es mayor que el segundo"
msg2="el segundo numero es mayor que el primero"
msg3="ambos numeros son igual"

def sumNumber(a,b):
    numC=a+b

    if a==b:
        print(msg3) 
    elif a<b:
        print(msg2) 
    else:
        print(msg1) 
        
    print("el resultado es: ", numC)    


        


sumNumber(4,numA)

sumNumber(35,numB)

sumNumber(numA,numB)
