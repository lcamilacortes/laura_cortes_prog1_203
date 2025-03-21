import random
 
def llenarLista(cantidad):
     lista=[]
     for i in range(cantidad):
         num=random.randint(1,100)
         lista.append(num)
     return lista
 

def menorlista(lista):
    
    menor1=100
    
    for m in lista:
        if m<menor1:
           menor1=m
    return menor1     
vec1=llenarLista(random.randint(3,10))
vec2=llenarLista(random.randint(3,10))
vec3=llenarLista(random.randint(3,10))
 

print(f"la lista es:{vec1}")
print( f"los menores son:{menorlista(vec1)} ")
#print(f"la lista es:{vec2}")
#print( f"los mayores son:{mayorlista(vec2)} ")
# print(f"la lista es:{vec3}")
# print( f"los mayores son:{mayorlista(vec3)} ")