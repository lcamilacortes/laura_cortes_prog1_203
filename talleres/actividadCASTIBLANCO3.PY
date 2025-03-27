def numeros_positivos():
    cont = 0
    numero=1 
    while numero>0:    
        numero=int(input("ingrese numeros"))
        cont+=1
    return cont-1
print(numeros_positivos())       