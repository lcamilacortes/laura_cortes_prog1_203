#Pedir 3 numeros e indicar cual de ellos es el valor del medio. Ej 11, 2 1000, el 
#valor del medio es 11. No use operadores lógicos
num1= int(input("ingrese el primer numero"))
num2= int(input("ingrese el segundo numero"))
num3= int(input("ingrese el tercer numero"))
if num2<num1<num3 or num3<num1<num2:
     print("el valor del medio es",num1)
elif num1<num2<num3 or num3<num2<num1:
     print("el valor del medio es",num2)
else:
     print("el valor del medio es",num3)
     