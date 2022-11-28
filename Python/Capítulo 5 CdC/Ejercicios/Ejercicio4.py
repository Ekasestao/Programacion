while True:
    try:
        cdc=input('\nIntroduzca una cadena: ')
        if len(cdc)>=1:
            break
        else:
            print('\nIntroduzca un valor correcto')    
    except:
        print('\nIntroduzca un valor correcto')

cdc=cdc.replace(' ','*')
print(cdc.title())