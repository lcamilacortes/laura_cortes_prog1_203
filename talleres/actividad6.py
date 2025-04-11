#pedir un número entre 0 y 9.999 y decir cuantas cifras tiene. Cuando el número exceda los límites emita un mensaje y finalice el programa
num1=int(input("digite un numero entre 0 y 9999"))

if num1<10:
        print("tiene 1 cifra")
elif num1<100:
        print("tiene 2 cifras")
elif num1<1000:
        print("tiene 3 cifras")
elif num1>=1000 and num1<9999:
        print("tiene 4 cifras")
else:
        print("digito por fuera de los limite")