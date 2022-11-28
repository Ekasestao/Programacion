'''

*Las colas constan de un conjunto de datos tipo "FIFO"
*Como si fuese una cola del banco, el primero en ser colocado será el primero en salir
*En Python existen las "colas" pero es más sencillo simularlo con listas

'''

cola=['Ekaitz','Oihane','Anaís','Nube','Leo']
cola.append('Susi')
print(cola)

print()

n=cola.pop(0)
print(f'Estamos atendiendo a {n}')
print(cola)