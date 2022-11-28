while True: #Primer valor del rango
    try:
        n=int(input('Introduzca el primer valor del rango: '))
        break
    except:
        print('Introduzca un valor válido')

while True: #Segundo valor del rango
    try:
        n2=int(input('Introduzca el segundo valor del rango: '))
        break
    except:
        print('Introduzca un valor válido')

suma=0

for e in range(n,n2+1): #Añadimos "+1" a "n2" ya que en "for in range()" el rango es abierto
    if e%2==0: #Si el número es par entonces lo suma
        suma+=e

print(suma)