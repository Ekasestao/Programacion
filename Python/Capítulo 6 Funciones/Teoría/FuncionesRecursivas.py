'''

*Son funciones que se llaman a si mismas
*Funcionan como bucles
*Tienen un caso base y un caso recursivo

'''

def cuenta_regresiva(n):
    if n==0: #Caso base
        print('Boom!')
    else: #Caso recursivo
        print(n)
        cuenta_regresiva(n-1)

cuenta_regresiva(5)