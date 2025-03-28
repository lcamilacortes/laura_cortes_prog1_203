#son datos estructurados, una clase es la definicxion de objetos, objeto: instancia de una clase. es la creaqcion de una clase. iterable, que lo puedo recorrer con indices
#add= agregarle elementos al conjunto update= se le puede agregar otros datos estructurados iterables como tuplas, listas y otros conjuntos, el set no es indexable, porque no tiene posiciones
#remove=elimina elementos pero manda error si el elemento no existe, discard=remueve elementos aunque no existan sin mandar error. pop= elimina y devuelve un numero aleatorio (aunque parece qu eborra siempre el menor)
#clear=elimina todo el conjunto, o sea, lo vacia nuevamente. operaciones de conjunto: cuando dice devuelkve significa que me va a entregar ese conjunto. union, interseccion,| pipe, & ampersant, - diferencia, ^ circunflejo.
#issubset=busca si es subconjunto del otro
# issuperset= busca si es un super conjunto es decir si contiene al otro
# c1=set()
# c1.add(10)
# print(c1)
# c1.add(11)
# print(c1)
# lista=[9,8,7]
# tupla=(23,24,25,26,9,7,8)
# c2={55,56}
# c1.update(c2)
# print(c1)
# c1.update(lista)
# print(c1)
# c1.update(tupla)
# print(c1)
# for elemento in c1:
#  print(elemento)
import random


a={0,1,2,3,4,5,7,9}
b={1,3,6,7,8,9,0}
print(a)
print(b)
union=a|b
print(f"union{union}")
inter=a&b
print(f"interseccion{inter}")
diferencia=a-b
print(f"diferencia{diferencia}")
difsimetrica=a^b
print(f" diferencia simetrica{a^b}")
conjunto=set()
conjunto2=set()
tam=random.randint(5,15)
for i in range(tam):
    num=random.randint(1,20)
    conjunto.add(num)
tam=random.randint(5,15)
for i in range(tam):
    num=random.randint(1,20)
    conjunto2.add(num)    


print(conjunto)
print(conjunto2)
union=conjunto|conjunto2
print(f"union{union}")
inter=conjunto&conjunto2
print(f"interseccion{inter}")
diferencia=conjunto-conjunto2
print(f"diferencia{diferencia}")
difsimetrica=conjunto^conjunto2
print(f" diferencia simetrica{conjunto^conjunto2}")

print("subset1= ", diferencia.issubset(conjunto))
print("subset2= ", diferencia.issubset(conjunto2))
print("superset1= ", union.issuperset(conjunto))
print("superset2= ", union.issuperset(conjunto2))

