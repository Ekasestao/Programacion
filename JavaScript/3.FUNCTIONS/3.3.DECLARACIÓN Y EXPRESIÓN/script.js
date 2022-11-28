var age = 3;

if (age <= 10) {
    var buildMenu = function () {  //Expresión de Función
        return 'Kids menu';
    };

    function buildMenuTwo() {
        return 'Kids menu again';  //Declaración de Función
    }

    console.log(buildMenu());
    console.log(buildMenuTwo());
}