var str = 'The quick brown fox jumped over the lazy dog'
console.log(str.length) //Devuelve la cantidad de cáracteres de la CdC
console.log(str.charAt(2)) //Devuelve el valor de la CdC del indice proporcionado
console.log(str.charAt(200))
console.log(str.concat(' again')) //Añade al final de la CdC el dato que proporcionemos
console.log(str.includes('quick')) //Devuelve valor booleano (True o False) si incluye la CdC proporcionada
console.log(str.startsWith('The')) //Devuelve valor booleano si la CdC empieza con el conjunto o caracter proporcionado
console.log(str.endsWith('lazy dog')) //Devuelve valor booleano si la CdC termina con el conjunto o caracter proporcionado
console.log(str.repeat(2)) //Repite la CdC una detrás de otra
console.log(str.match('over')) //Devuelve la CdC que coincida con la proporcionada
console.log(str.replace('fox', 'wolf')) //Remplaza el primer argumento por el segundo
console.log(str.search()) //Devuelve el índice de la CdC que coincida con la CdC proporcionada
console.log(str.indexOf('jumped')) //Devuelve el índice del primer caracter o CdC que coincida con la CdC proporcionada
console.log(str.lastIndexOf('o')) //Devuelve el índice del último caracter o CdC que coincida con la CdC proporcionada
console.log(str.slice(10)) //Devuelve la CdC que quede a la derecha del índice proporcionado
console.log(str.slice(-8)) //Devuelve la CdC que quede a la derecha utilizando índices negativos
console.log(str.slice(4, 9)) //Devuelve la CdC que quede entre el margen de índices proporcionados
console.log(str.trim()) //Devuelve la CdC sin espacios
console.log(str.slice(4, 10).trim()) //Como combinar varias funciones
console.log(str.toUpperCase()) //Devuelve la CdC a mayúsculas
console.log(str.toLowerCase()) //Devuelve la CdC a minúsculas