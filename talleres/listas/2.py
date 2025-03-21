#Sumar posiciones pares e impares (por separado),3. sumar valores pares
4. #Sumar valores impares
import random
 
def llenarLista(cantidad):
     lista=[]
     for i in range(cantidad):
         num=random.randint(1,100)
         lista.append(num)
     return lista
 
def sumaLista(lista):
     suma=0
     for num in lista:
         suma+=num
     return suma
 
def sumaParLista(lista):
     suma=0
     for num in lista:
         if num%2==0:
             suma+=num
     return suma
 
def sumaImparLista(lista):
     suma=0
     for num in lista:
         if num%2!=0:
             suma+=num
     return suma
 
vec1=llenarLista(random.randint(5,10))
vec2=llenarLista(random.randint(5,10))
vec3=llenarLista(random.randint(5,10))
 
print(f"la lista es {vec1}")
print(f"la suma de la lista es {sumaLista(vec1)}")
print(f"la suma par es {sumaParLista(vec1)}")
print(f"la suma impar es {sumaImparLista(vec1)}")
print(f"la lista es {vec2}")
print( f"la suma de la lista es {sumaLista(vec2)}")
print(f"la suma par es {sumaParLista(vec2)}")
print(f"la suma impar es {sumaImparLista(vec2)}")
print(f"la lista es {vec3}")
print(f"la suma de la lista es {sumaLista(vec3)}")
print(f"la suma par es {sumaParLista(vec3)}")
print(f"la suma impar es {sumaImparLista(vec3)}")