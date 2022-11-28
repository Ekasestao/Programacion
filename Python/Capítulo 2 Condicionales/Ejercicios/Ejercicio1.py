'''

*Determina cual de los dos números es par o si ambos lo son

'''

n1=int(input('Digite un número: '))
n2=int(input('Digite otro número: '))

if n1%2==0 and n2%2==0:
    print('Ambos números son pares')
elif n1%2==0 and n2%2!=0:
    print(f'{n1} es par')
elif n1%2!=0 and n2%2==0:
    print(f'{n2} es par')
else:
    print('Ambos números son impares')