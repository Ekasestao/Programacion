def cambio_ed(euros):
    return euros*1.07
def cambio_de(dolares):
    return dolares*0.94

while True:
    print('''\n\t.:MENÚ:.
1.Convertir Euros a Dólares
2.Convertir de Dólares a Euros
3.Salir''')
    while True:
        try:
            o=int(input('\nDigite una operación: '))
            if 4>=o>=1:
                break
            else:
                print('\nDigite un valor correcto')
                continue
        except:
            print('\nDigite un valor correcto')

    if o==1:
        euros=float(input('\nDigite la cantidad de euros: '))
        print(f'\nDólares -> {cambio_ed(euros):.2f}€')

    elif o==2:
        dolares=float(input('\n\nDigite la cantidad de dólares: '))
        print(f'\nEuros -> {cambio_de(dolares):.2f}$')

    elif o==3:
        print('\nAdios!\n')
        break
    else:
        print('\nDigite un valor correcto')