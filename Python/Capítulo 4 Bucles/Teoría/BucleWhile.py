'''

*Es un bucle con un número inderterminado o determinado de iteraciones
*Necesita un valor "booleano" para determinar el ciclo

'''

from math import sqrt

numero=int(input('Digite su número: '))

while numero<0: #Si el número es negativo cumple la condición y activa el bucle "while"
    print('Introduzca un número válido')
    numero=int(input('Digite su número: '))

raiz=sqrt(numero)

if round(raiz,0)==raiz: #Método personal para que los números naturales no tengas 2 decimales y los flotantes sí
    print(f'El resultado es {raiz:.0f}')
else:
    print(f'El resultado es {raiz:.2f}')

print()

i=0 #Iterador comienza en 0

while i<=10: #Si el valor de i es menor o igual a 10
    print(i,end='-') #Imprime el valor "i" hasta que este llegue a 10
    i+=1 #Añadimos 1 al iterador, si no el bucle será infinito y no lograremos nada