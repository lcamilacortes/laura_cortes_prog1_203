#Un obrero necesita calcular su salario semanal, el cual se obtiene de la sig. 
#manera:
#Si trabaja 40 horas o menos se le paga $2600 por hora
#Si trabaja más de 40 horas se le paga $2600 por cada una de las primeras 40 
#horas y $5000 por cada hora extra

horast = int(input ("Horas trabajadas?"))
horario1 = 2600
horario2 = 5000

if horast <= 40:
    salario = horast * horario1
    print ("Su salario es", salario)

else: 
    salariob = 40 * horario1 
    horasa = horast - 40 
    extras = horasa * horario2
    salariob = salariob + extras

    print ("su salario con extras es", salariob) 