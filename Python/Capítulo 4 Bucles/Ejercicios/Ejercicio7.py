from random import randint

print('\n \t.:Juego adivina el número:.')

a=randint(0,100)
intentos=0

while True:
    try:
        n=int(input('\n \tPrueba suerte (0-100): '))
        break
    except:
        print('\n \tIntroduzca un número entero')

while n!=a:
    if n<a:
        n=int(input('\n \tEl número es mayor: '))
        intentos+=1
    elif n>a:
        n=int(input('\n \tEl número es menor: '))
        intentos+=1
intentos+=1
print(f'\n \tFelicidades! Has adivinado el número {a} \n \tSolo has tardado {intentos} intentos')