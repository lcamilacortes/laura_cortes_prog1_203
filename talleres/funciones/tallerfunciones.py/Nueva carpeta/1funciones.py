
lista=[100 for i in range(10)]
print(lista)

lista=[i for i in range(10)]
print(lista)

lista=[i*i for i in range(1,11)]
print(lista)

import random
num=random.randint(5,15)
lista=[i for i in range(1,num)]
print(lista)

num=random.randint(5,15)
lista=[random.randint(1,100) for i in range(1,num)]
print(lista)


#cadena="estoy juicioso en progamacion 1"
#print(f"caracteres={len(cadena)}")
#for letra in cadena:
    #print(letra)

#list=[1,5,9,3,12,6]
#for x in lista:
    #print(x)
#pares=[x for x lista if x%2==0]
#impares=[x for x lista if x%2==0]
#print(pares)
#print(impares)
#impares=[]
#for x in lista:
    #if x%2==0:
        #print(f"{x} es par")
        #pares.append(x)
    #else:
        #print(f"{x}es impar")
        #impares.append(x)