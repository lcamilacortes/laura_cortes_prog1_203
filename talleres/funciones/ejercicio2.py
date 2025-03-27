#Encontrar un número natural n más pequeño tal que la suma
#de los n primeros números naturales (1 + 2 + 3 + 4…..)
#exceda de una cantidad (máximo) introducida por el teclado.
#Es decir cuantos números de la serie de los naturales debo
#sumar para superar el dato máximo.

def numax(num):
 cont=0
 acumulacion=0

 while acumulacion <= num:
    cont +=1
    acumulacion += cont

 return f"{cont} es el numero maximo"

print(numax(7))
print(numax(6))
print(numax(5))
print(numax(4))
print(numax(3))