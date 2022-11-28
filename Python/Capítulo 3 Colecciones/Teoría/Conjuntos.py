'''

*En los conjuntos los elementos se agregan de forma desordenada 
*Si en un conjunto hay elementos que se repiten solo mostrará el primer elemento repetido
*Para crear un conjunto VACÍO debemos asignar =set() porque al poner solo {} Python lo confunde con un diccionario| Conjunto=set()
*No puede tener dentro otro tipo de colección (tupla() y/o lista[])

'''
conjunto=set()
conjunto.clear()
conjunto={40,5.67,'Ekaitz'}
conjunto.add(5)
conjunto.discard(40)

print(conjunto)
print('Ekaitz' in conjunto)
print('Ekaitz' not in conjunto)

print()

a=frozenset({1,2,3}) #Convierte en inmutable(no se puede modificar como las tuplas) el conjunto
b={3,4,5}
c={2,3,1,5}
union=a|b #La unión es la suma de los elementos de ambos conjuntos dando como resultado todos los elementos una única vez
interseccion=a&b #La intersección son los elementos que se encuentran en ambos conjuntos 
diferencia=a-b #La diferencia son los elementos que están en el primer conjunto y no en el segundo
dif_asimetrica=a^b #La diferencia asimétrica es lo contrario de la intersección, los elementos que no se repiten en ambos conjuntos

print(a==b)
print(len(a))
print(union)
print(interseccion)
print(diferencia)
print(dif_asimetrica)
print(a.issubset(c)) #Indica si el conjunto "a" es un subconjunto(todos los elementos de "a" están en "c") de "c"
print(b.issubset(c))
print(c.issuperset(a)) #Indica si el conjunto "c" es un superconjunto(todos los elementos de "a" están en "c") de "a"
print(a.isdisjoint(b)) #Indica si el conjunto "a" no tiene ninguna unión con el conjunto "b"(se repite algún elemento)