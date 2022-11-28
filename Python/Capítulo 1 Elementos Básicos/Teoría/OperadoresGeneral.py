'''
Prioridad de los Operadores en General
1|()
2|**
3|*,/,%,not
4|+,-,and
5|>,<,==,>=,<=,!=,or
'''
a=10;  b=15; c=20
resultado=not(((a**2<b*c)or(c>b%a))and(b+a<c))
print(resultado)