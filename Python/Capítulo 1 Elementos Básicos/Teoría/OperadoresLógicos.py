'''

*Permite construir expresiones lógicas, se obtiene como resultado booleanos

-Operador AND:																			Prioridad de los Operadores Lógicos
Operando1	Operador	Operando2	Resultado											1|NOT
True		and			True		True												2|AND
True		and			False		False												3|OR
False		and			True		False
False		and			False		False

-Operador OR:
Operando1	Operador	Operando2	Resultado
True		or			True		True
True		or			False		True
False		or			True		True
False		or			False		False

-Operador NOT:
Operando	Resultado
not(True)	False
not(False)	True

'''

a=10; b=12; c=13; d=10
print(((a>b)or(a<c))and((a==c)or(a>=b)))