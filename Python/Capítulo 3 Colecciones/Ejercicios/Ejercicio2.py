lista1=set([1,2,3,'Ekaitz',3])
lista2=set([3,4,5,6,5])

uni=list(lista1|lista2)
dif=list(lista1-lista2)
dif2=list(lista2-lista1)
inter=list(lista1&lista2)

print(uni)
print(dif)
print(dif2)
print(inter)