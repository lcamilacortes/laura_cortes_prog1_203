

# lista=[100]
# x=90
# escalar=100
# tupla=(100,)
# print(type(lista))
# print(type(tupla))
# lista.append(12)
# tupla.append(100)#esta mal
# t=(1,2)
# print(type(t))
# print(t)
# t=t+(10,)
# print(t)
#mayor
import random
def llenarLista(cantidad):
     lista=[]
     for i in range(cantidad):
         num=random.randint(1,100)
         lista.append(num)
     return lista
 
def mayorlista(lista):
    
    mayor1=0
    
    for m in lista:
        if m>mayor1:
            mayor1=m
         
    return mayor1   

def menorlista(lista):
    
    menor1=100
    
    for m in lista:
        if m<menor1:
           menor1=m
    return menor1 

def promedioLista(lista):
    promedio=0
    sum=0
    total=len(lista)
    for num in lista:
        sum = sum + num
    promedio=sum/total
    return promedio

def sumaLista(lista):
     suma=0
     for num in lista:
         suma = suma + num
     return suma

def primo(num):
    cont=0
    for i in range(1,num+1):
        if num%i==0:
            cont+=1
    if cont==2:
        return True
    else:
        return False
    
def contarPrimos(lista):
    total_primos = 0

    for num in lista:
        if primo(num):
            print(f"{num} es primo")
            total_primos += 1
    
    return total_primos


lista1=llenarLista(random.randint(3,15))
print(lista1)

print(f"el mayor es {mayorlista(lista1)}")
print(f"el menor es {menorlista(lista1)}")
print(f"El promedio es {promedioLista(lista1)}")
print(f"la suma de la lista es {sumaLista(lista1)}")
print(f"El total de primos de la lista es {contarPrimos(lista1)}")



