#def saludar():
    #return "hola"#variaciones de la mquinikta,la puedo llamar las veces que quiera, la funcion le entrega su cadena de texto, no todas retornan, la mayoria si, el retorno serviria para finalaizar la funcion. la entrada se llama parametro. le puedo pasar cualquier nombtre

#print(saludar())
#def saludar():
   # return f"hola {nombre}"
#print(saludar("titoi"))
#print(saludar("tato"))
#print(saludar("teto"))
#print(saludar("tata"))

def perfecto(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    if sum==num:
        return f"{num} es perfecto"    
    else:
        return f"{num}no es perfecto"    