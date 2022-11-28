var someUser = {
    name: 'Ekaitz'
}

function nameFormatter(user) {
    console.log(user.name = 'Oops');  //Los objetos son tratados por referencia, reemplaza el valor original
}

nameFormatter(someUser);
console.log(someUser)

var someName = 'Ekaitz'

function nameFormatterTwo(name) {
    console.log(name = 'Oops');       //Si no, son tratados por valor, hace una copia sin modificar el original
}

nameFormatterTwo(someName);
console.log(someName)

someUser.name = 'Ekaitz';

function nameFormatter(userNameTwo) {
    console.log(userNameTwo = 'Oops');  //Hacer que un objetos sea tratado por valor
}

nameFormatter(someUser.name)
console.log(someUser.name)