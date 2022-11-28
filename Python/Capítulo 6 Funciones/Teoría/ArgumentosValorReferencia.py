'''

*Argumentos por valor| Variables simples: CdC, booleano, enteros...
*Argumentos por referencia| Colecciones: Listas, tuplas, diccionarios...

'''

def doblar(n):
    n*=2

n2=5
doblar(n2) #Argumento por valor(no modifica el valor de la variable asignada a la función)
print(n2)

def doblar2(n3):
    return n3*2

n4=5
n4=doblar2(n4) #Argumento por referencia(modifica el valor de la variable asignada a la función)
print(n4)

def doblar3(n5):
    for i,n6 in enumerate(n5):
        n5[i]*=2

n6=[5,10,15,20]
doblar3(n6) #Una colección se pasa por referencia(modifica el valor de la variable asignada a la función)
print(n6)

def doblar4(n7):
    for i2,n8 in enumerate(n7):
        n7[i2]*=2

n8=[5,10,15,20]
doblar4(n8[:]) #Para que pase por valor se añade [:] despues de la variable asignada a la función
print(n8)
