from operator import le


while True:
    try:
        cdc1=input('\nIntroduzca una palabra: ')
        break
    except:
        print('\nIntroduzca un valor correcto')

while True:
    try:
        cdc2=input('\nIntroduzca otra palabra: ')
        break
    except:
        print('\nIntroduzca un valor correcto')

if len(cdc1)<len(cdc2):
    print('\nLa segunda palabra tiene más caracteres\n')
elif len(cdc1)>len(cdc2):
    print('\nLa primera palabra tiene más caracteres\n')
elif len(cdc1)==len(cdc2):
    print('\nSon iguales\n')