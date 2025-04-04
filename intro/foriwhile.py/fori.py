
#->Patrón de triángulo numérico: Escribe un programa que imprima un triángulo de números con n filas, donde cada fila contiene el número de la fila repetido (por ejemplo, para n = 5, se imprimiría 
#1 
#22
#333
#4444
#55555




n = int(input("Digite un valor "))


for i in range(1, n + 1, ):  
    for j in range(1, i + 1):  
        print(i, end=" ")  
    print()  