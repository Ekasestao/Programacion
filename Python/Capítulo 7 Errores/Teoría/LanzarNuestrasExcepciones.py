def verificarEdad(edad):
    if edad<=0:
        raise ValueError('La edad no puede ser negativa')
    elif edad<18:
        print('Eres muy joven')
    elif edad<30:
        print('Eres joven')
    elif edad<50:
        print('Eres maduro')
    
edad=int(input('Digite su edad:' ))
try:
    verificarEdad(edad)
except ValueError as NegativeError:
    print(NegativeError)