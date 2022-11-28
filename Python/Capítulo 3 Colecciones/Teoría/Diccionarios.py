'''

*Los diccionarios al igual que los conjuntos{} agregan los elementos de forma desordenada
*Tienen dos elementos por posición(clave:valor)
*Puede tener otras colecciones en su interior inclusive otros diccionarios

'''

diccionario={'azul':'blue','rojo':'red','verde':'green'}
diccionario['amarillo']='yellow'
del(diccionario['verde'])

print(diccionario)
print(diccionario['rojo'])

print()

agenda={'Ekaitz':{'edad':20,'altura':1.80},'Oihane':[19,1.49],'Anais':[2.5,0.50]}
print(agenda)
print(agenda['Ekaitz'])

print()

equipo={10:'Messi',11:'Neymar',9:'Luis Suarez',1:'Ter-Stegen'}

print(equipo)
print(len(equipo))
print(equipo[10])
print(equipo.get(10,'No existe')) #Equipo.get() detecta si existe la clave en el diccionario y si no retorna un mensaje
print(10 in equipo)
print(equipo.keys()) #Equipo.keys() muestra solo las claves del diccionario
print(equipo.values()) #Equipo.values() muestra solo los valores del diccionario
print(equipo.items()) #Equipo.items() muestra los elementos, separados por tuplas
equipo.clear()
print(equipo)