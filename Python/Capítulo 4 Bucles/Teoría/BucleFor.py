'''

*Es un bucle con un número variable de iteraciones según los elementos de cada colección
*El bucle "for" se utiliza con colecciones(Listas[],Tuplas(),Diccionarios{})
*Recorre la colección asignando a la variable "e" el valor de cada elemento a medida que recorre la colección

'''

from os import sep


tupla=(1,2,3,4,5) #Este método funciona con tuplas(),listas[] y conjuntos{}
for e in tupla: #"For e in" recorre la colección elemento por elemento repitiendo el bucle hasta recorrer la colección
    print('Ekaitz')
    print(e)

print()

diccionario={'Ekaitz':20,'Oihane':19,'Anais':4} #Al tener dos valores en un mismo elemento debemos realizarlo de esta manera
for e in diccionario:
    print(f'{e}') #Imprime solo las claves del diccionario

print()

for e in diccionario:
    print(f'{diccionario[e]}') #Imprime solo los valores del diccionario

print()

for e in diccionario:
    print(f'{e}:{diccionario[e]}') #Imprime las claves y los valores del diccionario| NO RECOMENDADO

print()

for clave,valor in diccionario.items():
    print(f'{clave}:{valor}') #Imprime las claves y los valores del diccionario| RECOMENDADO

print()

cadena='Ekaitz'
for e in cadena:
    print(e,end='') #Añade cada caracter de esta cadena a una variable y con end='' indicamos que no haya salto de linea ni espacios