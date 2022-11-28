while True:
    try:
        cdc=input('\nIntroduzca una cadena: ')
        break
    except:
        print('\nIntroduzca un valor correcto')

cdc=cdc.replace(' ','')
cdc=cdc.lower()
cdcpa=cdc[::-1]

if cdc==cdcpa:
    print(f'\nLa cadena {cdc} es un palíndromo\n')
else:
    print(f'\nLa cadena {cdc} no es un palíndromo\n')