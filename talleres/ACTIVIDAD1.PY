# Escribe un programa que pida tres números y que escriba si son los tres
#iguales, si hay dos iguales o si son los tres distintos
n1=int(input("numero 1"))
n2=int(input("numero 2"))
n3=int(input("numero 3"))

if n1==n2 and n1==n3:
    print("son iguales")

elif n1==n2 or n1==n3 or n2==n3:
    print ("2 son iguales")
else:
    print ("son distintos")
    