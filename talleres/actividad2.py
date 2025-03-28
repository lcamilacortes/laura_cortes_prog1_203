#Pedir una nota de 0 a 10 y mostrarla de la forma: Insuficiente, Suficiente, Bien,
#etc. Use la escala que prefiera, pero cerciórese que tiene 5 valores
n1=int(input("ingrese nota de 1 a 5"))

if n1==0 or n1<=2.9: 
    print(" insuficiente")

elif n1==3 or n1<=4.9:
    print ("suficiente")
else:
    print ("excelente")
    