def multiplicar(x,y): #Las funciones con dos o más valores y "return" retornan un valor y no una acción
    return x*y

print(multiplicar(4,3))
print(multiplicar(8,5))

def cdc(): #Si se retornan valores en el cuerpo de la función los guardará en una tupla
    return 'hola',45,[1,2,3]

c,n,l=cdc() #Para guardar los valores que retorna la función en variables
print(cdc())
print(c)
print(n)
print(l)