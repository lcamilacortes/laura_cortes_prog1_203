#5. En un juego de preguntas a las que se responde “Si” o “No” gana quien 
#responda correctamente las tres preguntas. Si se responde mal a cualquiera de 
#ellas ya no se pregunta la siguiente y termina el juego. Las preguntas son:
#1. Colon descubrió América?
#2. La independencia de Colombia fue en el año 1810?
#3. The Doors fue un grupo de rock Americano?
pregunta1=(input(" Colon descubrió América?"))
if pregunta1!= "si":
    print ("incorrecta")

else:
    pregunta1=(input(" la independencia de Colombia fue en 1810?"))
    if pregunta1!= "si":
      print ("incorrecta")

    else:
       pregunta1= input("The Doors fue un grupo de rock americando?")
       if pregunta1!= "si":
          print ("Incorrecta")
       else:
         print("Se respondio corretamente todas las preguntas")