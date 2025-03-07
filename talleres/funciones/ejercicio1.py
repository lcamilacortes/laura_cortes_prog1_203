# Determinar si un numero es o no es primo

def primo(num):
 cont=0
 for i in range(1,num+1):
    if num%i==0:
        cont+=1
 if cont==2:
    return f"{num} es primo"
 else:
    return f"{num} no es primo"
    
print(primo(7))
print(primo(6))
print(primo(5))
print(primo(4))
print(primo(3))