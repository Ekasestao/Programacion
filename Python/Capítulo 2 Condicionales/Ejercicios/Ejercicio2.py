'''

*Determina que número es el mayor entre tres números

'''

n1=int(input('Ingrese el primer número: '))
n2=int(input('Ingrese el segundo número: '))
n3=int(input('Ingrese el tercer número: '))
if n1>=n2 and n1>=n3:
    print(f'El número más grande es el {n1}')
elif n2>=n1 and n2>=n3:
    print(f'El número más grande es el {n2}')
elif n3>=n1 and n3>=n2:
    print(f'El número más grande es el {n3}')