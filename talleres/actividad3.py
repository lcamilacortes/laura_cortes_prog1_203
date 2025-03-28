#Pida un numero al usuario que representa días del año. Diga a que mes del año
#corresponde así. Si el número es menor o igual a 31 indica que esta en enero,
#Pero si el número por ejemplo es 32 indica que es el 1 de febrero. No tenga en
#cuenta si el año es bisiesto, es decir siempre febrero tiene 28 días.
dias=int(input("ingresa numero de dias del año"))


if dias<=31:
    print("enero")

elif dias <=59:
    print ("febrero")
elif dias <=90:
    print ("marzo")
elif dias <=120:
    print ("abril")
elif dias <=151:
    print ("mayo")
elif dias <=181:
    print ("junio")
elif dias <=212:
    print ("julio")
elif dias <=243:
    print ("agosto")
elif dias <=273:
    print ("septiembre")
elif dias <=304:
    print ("octubre")
elif dias <=334:
    print ("noviembre") 
  
else:
    print ("diciembre")