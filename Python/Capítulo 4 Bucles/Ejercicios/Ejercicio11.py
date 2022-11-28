agenda={}
print('\n\t.:Bienvenido a tu agenda:.')
while True:
    print('\n\tMenú de opciones\n1.Nuevo contacto\n2.Borrar contacto\n3.Ver contactos existentes\n4.Salir')
    while True:
        try:
            operacion=int(input('\nIntroduzca la opción deseada: '))
            if 4>=operacion>=1:
                break
            else:
                print('\nIntroduzca una operación válida')
        except:
            print('\nIntroduzca una operación válida')
            continue

    if operacion==1:
        while True:
            try:
                nombre=input('\nIntroduzca el nombre del nuevo contacto: ')
                break
            except:
                print('\nIntroduzca un nombre válido')
        while True:
            try:
                numero=str(int(input('\nIntroduzca el número del nuevo contacto: ')))
                if 8<len(numero)<10:
                    break
                else:
                    print('\nIntroduzca un número valido')
                    continue
            except:
                print('\nIntroduzca un número válido')
        if nombre not in agenda and numero not in agenda:
            agenda[nombre]=numero
            print(f'\nEl contacto {nombre} se agregó correctamente')
        elif nombre in agenda:
            print(f'El nombre {nombre} ya existe en su agenda')
        elif numero in agenda:
            print(f'El número {numero} ya existe en su agenda')
    elif operacion==2:
        while True:
            try:
                nombre2=input('\nIntroduzca el nombre del contacto a eliminar: ')
                if nombre2 in agenda:
                    del(agenda[nombre2])
                    print(f'\nEl contacto {nombre2} se eliminó correctamente')
                    break
                else:
                    print('\nEste nombre no se encuentra en tu lista de contactos')
                    continue
            except:
                print('\nIntroduzca un nombre válido')
    elif operacion==3:
        print('\n\tAgenda de contactos')
        for clave,valor in agenda.items():
            print(f'\nNombre: {clave} | Número: {valor}')
    elif operacion==4:
        print('\nHasta luego!\n')
        break