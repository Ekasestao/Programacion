from math import pi

radio=float(input('Valor del radio: '))
longitud=2*pi*radio
area=pi*radio**2

'''

*{:.nf} es para modificar el número de decimales

'''
print(f'La longitud es de {longitud:.2f}')
print(f'El área es de {area:.2f}')