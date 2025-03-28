
#->Secuencia de Fibonacci hasta que supere un valor: Crea un programa que genere la secuencia de Fibonacci hasta que el valor de los términos sea mayor que un número x introducido por el usuario


n=int (input("digite hasta que numero desea su serie fibonacci"))
a,b=0,1

while a<=n:
   print(a)

   a,b= b,a+b

      
    