
def factorial(n):
    if n==0: #Caso base
        resultado=1
    else: #Caso recursivo
        resultado=n*factorial(n-1)
    return resultado

print(f'\n{factorial(8)}\n')