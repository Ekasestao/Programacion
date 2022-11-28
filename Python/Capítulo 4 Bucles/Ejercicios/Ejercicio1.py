from re import I


lista=[] #Con el bucle "while"| NO RECOMENDADO
i=1
while i<=50:
    lista.append(i)
    i+=1

for e in lista:
    print(e,end='-')

print()

lista2=list(range(1,51)) #Con el bucle "range()"| RECOMENDADO

for e in lista2:
    print(e,end='-')