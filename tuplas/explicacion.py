#listas
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


#tuplas
import random
def crearTupla():
 tupla=()
 cantidad=random.randint(5,15)
 for i in range(cantidad):
    tupla+=(random.randint(1,100), )
 return tupla
tupla2=crearTupla()
print(tupla2)   



def sumaTupla(tupla):
     suma=0
     for num in tupla:
         suma = suma + num
     return suma

print(sumaTupla(tupla2))

def meanTupla(tt):
   return sumaTupla(tt)/len(tt)

print(meanTupla(tupla2))

def mayorTupla(t):
    
    mayor1=0
    
    for m in t:
        if m>mayor1:
            mayor1=m
         
    return mayor1   

def menorTupla(ttt):
    
    menor1=100
    
    for m in ttt:
        if m<menor1:
           menor1=m
    return menor1 

print(f"el mayor es {mayorTupla(tupla2)}")
print(f"el menor es {menorTupla(tupla2)}")