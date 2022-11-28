'''

Condicionales combinados
if x and y
elif x or y

'''

edad=int(input('Digite su edad: '))

if 100>=edad>=0:
    if edad>=18:
        print('Eres mayor de edad')
    else:
        print('Eres menor de edad')
else:
    print('Introduzca una edad valida')