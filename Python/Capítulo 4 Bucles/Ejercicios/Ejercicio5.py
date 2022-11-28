from math import factorial


while True:
    try:
        n=int(input('Introduzca un número positivo: '))
        if n>=0:
            break
        else:
            continue
    except:
        print('Introduzca un valor válido')
fact=factorial(n)

print(fact)