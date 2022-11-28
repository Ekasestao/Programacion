/* Un programa de C++ se compone de 2 elementos (la librería y la función principal)
Sin una de ellas el programa no funcionaría
*/

#include<iostream> //#include<librería> para importar una librería, iostream=input/output de datos

using namespace std; //Para no tener que escribir std:: antes de cout<<

int main(){ //Para crear nuestra función principal

    cout<<"Hola mundo\n"; //Cout<<;=print() de Python

    return 0; //Siempre retornamos 0 para indicar que el programa acabó correctamente
}