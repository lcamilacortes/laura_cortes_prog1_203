#Pedir una nota de 0 a 10 y mostrarla de la forma: Insuficiente, Suficiente, Bien,
#etc. Use la escala que prefiera, pero cerciórese que tiene 5 valores
def n1(nota):

 if nota==0 or nota<=2.9: 
    return f"{nota} es insuficiente "

 elif nota==3 or nota<=4.9:
   return f"{nota} es suficiente "


 else:
   return f"{nota} es excelente "
 
print(n1(7))
print(n1(6))
print(n1(5))
print(n1(4))
print(n1(3))