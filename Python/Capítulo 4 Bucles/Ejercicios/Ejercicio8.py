saldo=1000
true=True
print('\n\t.:Bienvenido a BBVA:.')
while true:
    print('\n\tIndique una de las operaciones\n\n1.Ingresar\n2.Retirar\n3.Mostrar saldo\n4.Salir')
    while True:
        try:
            operacion=int(input('\nIntroduzca una operación: '))
            if 4>=operacion>=1:
                break
            else:
                print('\nOperación invalida')
        except:
            print('\nOperación invalida')        
    if operacion==1:
        print(f'\nSu saldo actual es de {saldo:.2f}€')
        while True:
            try:
                ingreso=int(input('\n¿Cuanto dinero desea ingresar?: '))
                if 1000000>=ingreso>=1:
                    break
                else:
                    print('\nIntroduzca una cantidad válida')
            except:
                print('\nIntroduzca una cantidad correcta') 
        saldo+=ingreso
        print(f'\nSu saldo actual es de {saldo:.2f}€')
        while True:
            try:
                o=str(input('\nDesea realizar otra operación?: ')).lower()
                if o=='si' or o=='sí' or o=='no':
                    break
                else:
                    print('\nIndique "Sí" o "No"')
            except:
                print('\nOperación invalida')
        if o=='si' or o=='sí':
            continue
        elif o=='no':
            print('\n\tSesión cerrada, vuelva cuando quiera!\n')
            true=False
    elif operacion==2:
        print(f'\nSu saldo actual es de {saldo:.2f}€')
        while True:
            try:
                retirada=int(input('\n¿Cuanto dinero desea retirar?: '))
                if 1000000>=retirada>=1:
                    break
                else:
                    print('\nIntroduzca una cantidad válida')
            except:
                print('\nIntroduzca una cantidad correcta')
        if retirada>saldo:
            print('\nSaldo insuficiente')
        else:
            saldo-=retirada
            print(f'\nSu saldo actual es de {saldo:.2f}€')
            while True:
                try:
                    o2=str(input('\nDesea realizar otra operación?: ')).lower()
                    if o2=='si' or o2=='sí' or o2=='no':
                        break
                    else:
                        print('\nIndique "Sí" o "No"')
                except:
                    print('\nOperación invalida')
            if o2=='si' or o2=='sí':
                continue
            elif o2=='no':
                print('\n\tSesión cerrada, vuelva cuando quiera!\n')
                true=False
    elif operacion==3:
        print(f'\nSu saldo es de {saldo:.2f}€')
        while True:
            try:
                o3=str(input('\nDesea realizar otra operación?: ')).lower()
                if o3=='si' or o3=='sí' or o3=='no':
                    break
                else:
                    print('\nIndique "Sí" o "No"')
            except:
                print('\nOperación invalida')
        if o3=='si' or o3=='sí':
            continue
        elif o3=='no':
            print('\n\tSesión cerrada, vuelva cuando quiera!\n')
            true=False
    elif operacion==4:
        print('\n\tSesión cerrada, vuelva cuando quiera!\n')
        true=False