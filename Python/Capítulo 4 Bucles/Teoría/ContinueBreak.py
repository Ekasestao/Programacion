'''

*Las instrucciones "continue" y "break" se pueden utilizar en todos los bucles anteriores
*La instrucción "continue" sirve para obviar las lineas que estén después de esta
*La instrucción "break" sirve para detener el ciclo actual
'''

for e in range(0,10):
    if e==5: #Si "e" es igual a "5" continuará sin imprimir en esta vuelta porque se ha "continuado"
        continue 
    print(e)

print()

for e in range(0,10):
    if e==5: #Si "e" es igual a "5" el ciclo se detendrá y no volverá a empezar
        break 
    print(e)