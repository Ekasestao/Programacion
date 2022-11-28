'''

*Las listas pueden modificarse y buscar en ellas
*Se pueden transformar listas a tuplas y viceversa con list() y tuple()

'''

lista=['Lunes','Martes','Miércoles','Jueves','Viernes',40,5.67,[1,2,3],True]
tupla=tuple(lista)
print(tupla)
print(lista)
print(len(lista))
lista[0]=8 #Lista[n]= sustituye el valor con el indice "n" de la lista por el valor que deseemos
lista[5]*=2 #Lista[n] operador(*)= modifica el valor con el indice "n" de la lista
print(lista)

print()

lista1=[1,2,4,5]
lista1.insert(2,3) #Lista.insert(indice,valor) introduce un valor en un índice concreto
lista2=[6,7,8]
lista3=lista1+lista2
lista3.append(9) #Lista.append() introduce un valor al final de la lista
lista3.extend([10,11,12]) #Lista.extend([]) introduce multiples valores al final de la lista
print(lista3)

print()

lista4=[1,2,3,4,5,'Ekaitz']
valor='Ekaitz'
if valor in lista4:
    print(valor in lista4)
    print(lista4.index(valor)) #Lista.index() devuelve el índice de posición del valor en la lista
else:
    print('El valor no esta en la lista')

print()

lista5=[1,2,3,4,5,'Ekaitz',1,2,3,1,2,1,'Ekaitz',2,1]
print(lista5.count('Ekaitz')) #Lista.count() cuenta cuantas veces se encuentra ese valor en la lista

print()

lista6=[1,2,3,4,5,'Ekaitz']
lista6.pop() #Lista.pop() elimina el último valor de la lista y Lista.pop(n) elimina el valor que esta en el índice "n"
print(lista6) #Print(Lista.pop()) Imprime y elimina el último valor de la lista y Print(Lista.pop(n)) imprime y elimina el valor que esta en el índice "n"

print()

lista7=[1,2,3,4,5,'Ekaitz']
lista7.remove('Ekaitz') #Lista.remove() elimina el valor de la lista que queremos en caso de no conocer su índice
print(lista7)

print()

lista8=[1,2,3,4,5,'Ekaitz']
lista8.clear() #Lista.clear() vacía la lista
print(lista8)

print()

lista9=[1,2,3,4,5,'Ekaitz']
lista9.reverse() #Lista.reverse() voltea el orden de la lista
print(lista9)

print()

lista10=[5,4,-7,9,0,1,3]
lista10.sort(reverse=True) #Lista.sort() ordena números enteros de menor a mayor y Lista.sort(reverse=True) ordena de mayor a menor
print(lista10)