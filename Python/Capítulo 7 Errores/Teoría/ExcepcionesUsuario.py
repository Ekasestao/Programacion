'''

*Hay dos tipos de errores: los originados por el programador y los originados por el usuario
*Tipos de excepciones del usuario: ValueError, ZerDivisionError
*Para solucionarlo puedes aislar el error y continuar con el programa o puedes bloquear el programa hasta solucionarlo

'''

try:
    n=int(input('Digite un número')) #No pasar a "int" el número introducido e intentar hacer operaciones númericas con él
    print(n)
except:
    print('Ha ocurrido un error')

while True:
    try: #Comprueba si hay un error al ejecutar el cuerpo de "try"
        n=int(input('Digite un número'))
        print(n)
    except: #Si hay un error ejecutará "except"
        print('Ha ocurrido un error')
    else: #Si no hay ningun error ejecutará "else"
        print('Programa finalizado correctamente')
        break
    finally:
        print('Iteración finalizada')

def dividir():
    while True:
        try:
            n=float(input('Digite un número: '))
            n2=float(input('Digite otro número: '))
            resultado=n/n2
            print(f'{resultado:.2f}')
        except ValueError:
            print('Error: Digite correctamente los números')
        except ZeroDivisionError:
            print('Error: No puede dividir entre 0')
        else:
            break

dividir()