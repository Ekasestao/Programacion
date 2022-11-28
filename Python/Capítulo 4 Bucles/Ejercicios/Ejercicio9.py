while True:
    try:
        cdc=input('\nIntroduza la cadena de caracteres o frase: ')
        break
    except:
        print('\nIntroduzca algún caracter')

print(f'\nFrase: {cdc}')

cdclimpio=''

for e in cdc:
    if e!=" ":
        cdclimpio+=e

cdc=cdclimpio

print(f'\nFrase final: {cdc}')
print(f'\nNº de caracteres: {len(cdc)}')