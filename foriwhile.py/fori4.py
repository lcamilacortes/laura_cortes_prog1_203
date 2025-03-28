

num1=int(input("ingrese el  numero"))
suma=0

while num1!=0:
    
    i = 1
    while i < num1:
        if num1 % i == 0:
            suma += i
        i += 1
    if suma == num1:
        perfectos += f"{num1} "
        cont += 1