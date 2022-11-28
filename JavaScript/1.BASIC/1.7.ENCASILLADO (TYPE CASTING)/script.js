var data = '100' - 42;

var data = 100 + null;

var data = '100' + 42;

console.log(data)

var data = + '100' + 42;

console.log(data)

var ageOne = 12;

var ageOne = String(ageOne);
console.log(ageOne)
console.log(typeof ageOne)

var ageOne = 12;

var ageOne = ageOne.toString();
console.log(ageOne)
console.log(typeof ageOne)

/* 
var ageTwo = '33'

var ageTwo = Number(ageTwo)
console.log(ageTwo)
console.log(typeof ageTwo)

var ageTwo = '33';

var ageTwo = parseInt(ageTwo);
var ageTwo = parseFloat(ageTwo);
console.log(ageTwo)
console.log(typeof ageTwo) */

/* La mejor manera de pasar CdC a numeros */

var ageTwo = '33';
var ageTwo = + ageTwo
console.log(ageTwo)
console.log(typeof ageTwo)

var boolean = + true;
console.log(boolean)

var boolean = + false;
console.log(boolean)