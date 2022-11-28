from operator import index


'''

*Las tuplas no se pueden modificar pero se puede buscar en ellas
*Se pueden transformar listas a tuplas y viceversa con list() y tuple()

'''

tupla=(40,5.67,[1,2,3],'Ekaitz',40)
lista=list(tupla)
print(lista)
print(tupla[0])
print('Ekaitz' in tupla)
print(tupla.index('Ekaitz'))
print(tupla.count(40))
print(len(tupla))