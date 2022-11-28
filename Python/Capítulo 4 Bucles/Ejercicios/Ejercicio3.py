lista=[]

while True: #Sirve para validar la entrada de datos de "input"
    try:
        n=int(input('Introduzca un número: ')) #Si consigue almacenar el valor se rompe el ciclo de validación
        break
    except: #Si no consigue almacenarlo, en vez de dar error imprime un mensaje y se intenta de nuevo
        print('Escriba un número válido.')
while n!=0: #Si el número es diferente a 0 guardará el número y volverá a pedir otro número
    lista.append(n)
    while True:
        try:
            n=int(input('Introduzca otro número: '))
            break
        except:
            print('Escriba un número válido.')
#Lista.append(n) si queremos añadir el "0" también a la lista
lista.sort() #Para ordenar la lista de manera ascendente
print(f'Su lista ordenada es la siguiente: {lista}')