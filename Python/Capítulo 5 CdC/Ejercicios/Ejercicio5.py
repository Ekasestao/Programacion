while True:
    try:
        cdc=input('\nIntroduzca una cadena: ')
        if len(cdc)>=1:
            break
        else:
            print('\nIntroduzca un valor correcto')    
    except:
        print('\nIntroduzca un valor correcto')

'''

Cuenta todas las vocales de la frase conjuntamente

'''

cdc=cdc.lower()
v='aeiouáéíóú'
vocales=0

for e in cdc:
    if e in v:
        vocales+=1

print(f'\n{vocales}')

'''

Cuenta todas las vocales de la frase individualmente

'''

print(f'\nVocal a: {cdc.count("a")}')
print(f'Vocal e: {cdc.count("e")}')
print(f'Vocal i: {cdc.count("i")}')
print(f'Vocal o: {cdc.count("o")}')
print(f'Vocal u: {cdc.count("u")}\n')