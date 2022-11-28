'''

*Las CdC son inmutables

'''

cadena="Hola \"mundo\"" #Las "\" antes de cada " indican que se quieren mostrar como mensaje literal
print(cadena)

cadena2=r"D:\nombre\trabajos" #Con "r" antes de las "" lo procesa crudo(raw), por ende ignora los "\" junto con una letra
print(f"\n{cadena2}")

cadena3='''Hola
Que tal?
Mi nombre es Ekaitz
Cual es el tuyo?
'''
print(f'\n{cadena3}')

cadena4='Hola '
cadena5='mundo'
print(f'\n{cadena4+cadena5}')

cadena6='Ekaitz'
print(f'\n{cadena6}\n{len(cadena6[2:5])}')

cadena7='Hola mundo'
print(f'\n{cadena7.upper()}') #Mayúsculas
print(f'\n{cadena7.lower()}') #Minúsculas
print(f'\n{cadena7.capitalize()}') #Primera letra mayúscula
print(f'\n{cadena7.title()}') #Primeras letras mayúsculas
print(f'\n{cadena7.islower()}') #Comprueba si toda la CdC está en minúscula
print(f'\n{cadena7.isupper()}') #Comprueba si toda la CdC está en mayúscula
print(f'\n{cadena7.istitle()}') #Comprueba las iniciales de cada palabra están en mayúscula
print(f'\n{cadena7.isspace()}') #Comprueba si toda la CdC está compuesta por espacios
print(f'\n{cadena7.startswith("h")}') #Comprueba si la CdC empieza con la cadena asignada
print(f'\n{cadena7.endswith("do")}') #Comprueba si la CdC termina con la cadena asignada
print(f'\n{cadena7.split()}') #Separa e introduce en una lista los elementos de la CdC separados por espacios o el caracter que decidamos
print(f'\n{"-".join(cadena7)}') #Separa los caracteres de la CdC por el caracter que nosotros decidamos
print(f'\n{cadena7.replace("mundo","a todos")}')

cadena8='1000'
cadena9='AsqT'
print(f'\n{cadena8.isdigit()}') #Siendo una CdC comprueba si está compuesto por puros valores numéricos
print(f'\n{cadena9.isalpha()}') ##Siendo una CdC comprueba si está compuesto por puros caracteres alfabéticos
print(f'\n{(cadena8+cadena9).isalnum()}') ##Siendo una CdC comprueba si está compuesto por numeros o caracteres alfabéticos

cadena10='     hola     '
print(f'\n{cadena10.strip()}') #Elimina los caracteres de la CdC que decidamos
