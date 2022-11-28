#include<iostream>

using namespace std;

int main(){
    int numero;

    cout<<"Digite su numero: "; cin>>numero;

    switch (numero)
    {
    case 1: cout<<"Es el numero 1"; break;
    
    default: cout<<"El numero no es 1"; break;
    }

    return 0;
}