def saludar(): #Las funciones con solo un valor no tienen "return" y ejecutan la acción almacenada en su cuerpo
    print('Hola')

saludar()

def saludar2(nombre):
    print(f'Hola {nombre}')

saludar2('Ekaitz')

def tabla_multiplicar(n):
    for i in range(1,11):
        print(f'{n}*{i}={n*i}')

tabla_multiplicar(5)