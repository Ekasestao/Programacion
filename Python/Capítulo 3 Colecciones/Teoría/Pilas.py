'''

*Las pilas constan de un conjunto de datos tipo "LIFO"
*Como si fuese una pila de libros, el último en ser colocado será el primero en salir
*En Python no existen las "pilas" como tal pero se pueden simular con listas

'''

pila=[1,2,3]
pila.append(4) #Pila.append(v) añade el valor al final de la pila
print(pila)

print()

n=pila.pop() #Pila.pop() elimina el último valor de la pila
print(f'Sacando el elemento {n}')
print(pila)