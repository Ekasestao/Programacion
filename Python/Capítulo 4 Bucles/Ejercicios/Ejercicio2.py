lista=list(range(1,11))
print(lista)

n=int(input('Digite un número: '))
i=0 #Iterador para aumentar el indice de "lista[i]=e" y que recorra toda la lista

for e in lista:
    lista[i]*=n #Para cualquier valor en la lista, se modificará el valor de "e" por el de "e*n"
    i+=1
print(lista)