var arr = ['Altuve', 'Bregman', 'Correa', 'Springer'];
console.log(arr)
console.log(arr.pop()) //Elimina el ultimo elemento de la matriz
console.log(arr.push('Baggwell')) //Añade un elemento al final de la matriz
var elementPop = arr.pop();  //Guarda el elemento eliminado en una variable
console.log(arr.shift()) //Elimina el primer elemento de la matriz
console.log(arr.unshift('Kyle')) //Añade un elemento al inicio de la matriz
var foundElement = arr.indexOf('Correa'); //Guarda el índice del elemento a eliminar en una variable
console.log(arr.splice(foundElement, 1)) //Elimina elementos indicando el índice y la cantidad de elementos a eliminar
console.log(arr.splice(1, 2)) //Elimina elementos indicando el índice y la cantidad de elementos a eliminar
console.log(arr)