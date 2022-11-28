while True:
    try:
        cdc=input('\nIntroduzca una cadena de caracteres: ')
        break
    except:
        print('Introduzca algún caracter')

lista=[]

for e in cdc:
    if e !=' ' and e not in lista:
        lista.append(e)
            
print(lista)