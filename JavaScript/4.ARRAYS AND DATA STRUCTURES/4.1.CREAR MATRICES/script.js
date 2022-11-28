var generatedArray = new Array(3);
console.log(generatedArray)
console.log(generatedArray.length)

var literalArray = ['Altuve', 'Correa', 'Spring'];
console.log(literalArray[0])
console.log(literalArray.length)

var mixedArray = ['Hi', 1, ['a', 'b','c'], { name:'Ekaitz'}, function greeting() {console.log('Hey there')}];
console.log(mixedArray)
console.log(mixedArray.length)
console.log(mixedArray[2][2])
console.log(mixedArray[3].name)
console.log(mixedArray[4]());