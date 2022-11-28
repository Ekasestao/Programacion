lista=[]

while True:
    try:
        n=int(input('Introduzca un número: '))
        break
    except:
        print('Introduzca un número entero')

for e in range(1,11):
    lista.append(e*n)

print(lista)