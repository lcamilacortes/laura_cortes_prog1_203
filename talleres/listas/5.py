#mayor
import random

def mayorlista(lista):
    
    mayor1=0
    
    for m in lista:
        if m>mayor1:
            mayor1=m

           
      
           
    return lista    
may1=mayorlista(random.randint(3,10))
may2=mayorlista(random.randint(3,10))
may3=mayorlista(random.randint(3,10))

print( f"los mayores son:{may1} ")
print( f"los mayores son:{may2} ")
print( f"los mayores son:{may3} ")