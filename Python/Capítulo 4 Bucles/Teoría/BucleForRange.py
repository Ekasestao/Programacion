'''

*Es un bucle con un número determinado de iteraciones
*El bucle "for" se utiliza con números enteros "range(n)" o con rangos "range(m,n+1)" ya que recorrera desde m hasta n-1
*Recorre la colección asignando a la variable "e" el valor de cada elemento a medida que recorre la colección imaginaria o el rango
*Se puede modificar la distancia a la que recorre la colección añadiendo una segunda coma después de n+1
'''

for e in range(50): #La cuenta de la colección imaginaria comienza desde 0 hasta el número seleccionado menos 1 (0,n-1)
    print(e)

print()

for e in range(5,11): #La colección "range(5,11)" contiene los valores desde el "5" hasta el "10"| (m,n-1)
    print(e)

print()

for e in range(2,21,2): #Para modificar la distancia de recorrido utilizamos "range(m,n+1,+/-d)"
    print(e)

for e in range(20,1,-2):
    print(e)