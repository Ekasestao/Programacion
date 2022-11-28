'''

*Hay dos tipos de errores: los originados por el programador y los originados por el usuario
*Tipos de errores del programador: sintácticos(SyntaxError, NameError) y semánticos(IndexError, TypeError)
*La única solución es arreglar manualmente el error cometido

'''

prin('Hola amigo' #No cerrar un parentesis u otro tipo de llave, o no escribir bien el nombre de una función

if 15>10 #No poner ":" después del condicional o función 
    print('Es mayor')

lista=[1,2,3] #Quitar más elementos de los que hay en la lista(SOLUCIONADO)
while len(lista)>0:
    lista.pop()
    print(lista)

lista=[1,2,3] #Buscar un índice en la lista que no existe
print(lista[4])

n=input('Digite un número') #No pasar a "int" el número introducido e intentar hacer operaciones númericas con él
print(n+10)