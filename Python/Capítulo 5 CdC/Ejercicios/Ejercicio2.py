while True:
    try:
        cdc=input('\nIntroduzca una palabra o frase: ')
        if len(cdc)>1:
            break
        else:
            print('\nIntroduzca un valor correcto')
    except:
        print('\nIntroduzca un valor correcto')

if cdc.endswith('.'):
    print('\nTermina con punto\n')
else:
    print('\nNo termina con punto\n')