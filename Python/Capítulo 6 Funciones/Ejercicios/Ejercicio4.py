from cgitb import reset


def sumar_digitos(n):
    if n==0: #Caso base
        resultado=0
    else: #Caso recursivo
        resultado=sumar_digitos(int(n/10))+(n%10)
    return resultado

print(f'\n{sumar_digitos(125)}\n')