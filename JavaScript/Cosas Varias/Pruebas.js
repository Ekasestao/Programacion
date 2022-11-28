/* let myNumber = parseInt(12);

let myNewString = String(myNumber);

console.log(myNumber)
console.log(typeof myNumber)
console.log(myNewString)
console.log(typeof myNewString) */

/* stringOne = "The dog meows"

replacedString =  stringOne.replace('dog', 'cat')
console.log(replacedString)
stringTwo = "The cow jumped over the moon"

indexOfOver =  stringTwo.indexOf('over')
console.log(indexOfOver)
stringThree = "Never gonna give you up never gonna let you down"

lastIndex = stringThree.lastIndexOf('never')
console.log(lastIndex) */

/* var str = "The five boxing wizards jump quickly";
console.log(str.slice(str.indexOf('w'))); */

/* answer = false;

if (answer === false) {
    console.log(answer = true)
} */

/* var age = 15;
    
if (age >= 15) {
    return true;
} else if (age < 20) {
    return false
} */

/* switch (0) {
    default:
        return 'number'
} */

/* function greeting() {
    return 'Hi there'
} */

/* var myFunction = function() {
    return true;
} */

/* function sum(arg1, arg2) {
    console.log(arg1 + arg2)
    return arg1 + arg2;
}
sum(2, 3); */

/* var someUser = {
    name: 'Blank'
};

function changeName(user) {
    console.log(someUser.name = 'Jordan');
    return someUser.name = 'Jordan';
}

changeName(someUser);
console.log(someUser) */

/* function movieTheater(){
    var seats = 50;
    var seatsSold = 28;

    return{
        remainingSeats: function(){
            return (seats - seatsSold)
        }
    }
}

var roomOne = movieTheater();

roomOne.remainingSeats(); */

/* class Person {
    constructor(name){
        this.name = name;
    }
}

const yourPerson = new Person('Jordan'); */

/* var seats = {
    seats: 50,
    seatsSold: 28,
    remainingSeats: function(){
        return (this.seats - this.seatsSold)
    },
    enoughSeats: function(){
        if(this.remainingSeats() > 0){
            return this.remainingSeats()
        }
    }
}

seats.enoughSeats() */

/* let array = Array(4);
array.push('Bagels'); */

/* var array = ['Altuve', 'Bregman', 'Correa', 'Springer'];

console.log(array.splice(3, 1)) */

/* members = [1, 2, 3, 4, 5];

for (var i = 0; i < members.length; i++) {
    console.log(members[i]);
} */

/* let user = { 
    username : 'Maria', 
    email : 'maria@example.com', 
    phone : '5555555' };

for (var key in user){ 
    console.log(key + "=>" + user[key]);
} */

/* var data = 0, dogHouse = ['Bella', 'Max', 'Luna', 'Lucy'];

while (data < dogHouse.length) {
    console.log(dogHouse[data]);
    data++;
} */

/* const selector = document.querySelectorAll('p'); */

/* const nodeList = document.querySelectorAll('.snake'); */