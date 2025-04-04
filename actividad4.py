#Telefónica realiza los cálculos del costo de una llamada de teléfono siguiendo
#los cálculos así:
#Cuando se descuelga el teléfono los primeros 3 minutos (banderazo) cuestan
#200 pesos y cada minuto adicional cuesta 50 pesos. Escriba un programa que
#permita calcular el costo de una llamada dados los minutos de duración.

n1=int(input("numero de minutos utilizados"))


if n1<=3:
    print(" $200")
else:
    m1=200+(n1-3)*50
    print(" el costo es", m1)




