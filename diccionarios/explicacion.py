persona= {"nombre":"angela martinez", "documento":1234566, "correo":"amartinez@mail.com", "clases":["programacion","algebra", "estadistica"], 
          "ubicacion":{"municipio":"soacha", "barrio":"san mateo"}
                       }
print(type(persona))
print(persona)
print(persona["ubicacion"])
print(persona["documento"])
persona["promedio"]=3.5
print(persona)

#persona.clear(), elimina todos los elementos del diccionario
x=persona.copy()
print(x)
#claves=("universidad", "programa"
#valores=none
##academia=dict.fromkeys(claves,valores)
#print(academia)
print(persona.keys())
print(persona.values())
print(persona.items())
for key in persona.keys():
    print(key)
for val in persona.values():
    print(val)
for item in persona.items():
    print(item)
    