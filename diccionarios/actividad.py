frutas={"naranja":"orange", "fresa":"strawberry", "banano":"banana", "manzana":"apple","pera":"pear","durazno":"peach","limon":"lemon","piña":"pineapple","coco":"coconut","mora azul":"blueberry",}
nuevaC=(input("digite fruta en español"))
if nuevaC in frutas.keys():
    print("el elemento ya se encuentra en el diccionario")
nuevoV=(input("digite a que es igual"))

if nuevoV in frutas.values():
    print("el elemento ya se encuentra en el diccionario")
else:    
 frutas["nuevaC"]=nuevoV
 print(frutas)

# if traduccion in frutas.keys():
#  print(frutas[traduccion])

# for key,value in frutas.items():
#  if traduccion==value:
#   print(key)

