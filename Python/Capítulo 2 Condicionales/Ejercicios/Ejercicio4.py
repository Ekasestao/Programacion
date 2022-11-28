import math

n1=float(input('Introduzca un número: '))
n2=float(input('Introduzca otro número: '))
operacion=(input('Introduzca la operación: ')).upper()

if operacion=='S':
    s=n1+n2
    print(f'{s:.2f}')
elif operacion=='R':
    r=n1-n2
    print(f'{r:.2f}')
elif operacion=='P' or operacion=='M':
    m=n1*n2
    print(f'{m:.2f}')
elif operacion=='D':
    d=n1/n2
    print(f'{d:.2f}')
else:
    print('Operación invalida')