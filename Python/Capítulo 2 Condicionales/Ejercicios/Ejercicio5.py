saldo=1000

operacion=int(input('\t.:MENÚ:.\n*1.Ingresar\n*2.Retirar\n*3.Mostrar saldo\n*4.Salir\n')).lower()

print()

if operacion=='1':
    dinero=float(input('¿Cuanto dinero desea ingresar?: '))
    saldo+=dinero
    print(f'Su saldo actual es de {saldo:.2f}€')
elif operacion=='2':
    dinero=float(input('¿Cuanto dinero desea retirar?: '))
    if dinero>saldo:
        print('Saldo insuficiente')
    else:
        saldo-=dinero
        print(f'Su saldo actual es de {saldo:.2f}€')
elif operacion=='3':
    print(f'Su saldo es de {saldo:.2f}€')
elif operacion=='4':
    print('Conexión cerrada, vuelva cuando quiera!')
else:
    print(f'Operación "{operacion}" invalida')