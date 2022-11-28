#include<iostream>
#include<math.h>

using namespace std;

int main(){
    int opc,cubo,par,resultado;

    cout<<"\t.:MENU:."<<endl;
    cout<<"1.Cubo de un numero"<<endl;
    cout<<"2.Par o impar"<<endl;
    cout<<"3.Salir"<<endl;
    cout<<"Opcion: "; cin>>opc;

    switch (opc){
        case 1:
            cout<<"\nDigite un numero: "; cin>>cubo;
            resultado=pow(cubo,3);
            cout<<"El cubo del numero es: "<<resultado<<endl; break;
        case 2:
            cout<<"\nDigite un numero: "; cin>>par;
            if (par%2==0){
                cout<<"\nEl numero "<<par<<" es par"<<endl;
            }
            else{
                cout<<"\nEl numero "<<par<<" es impar"<<endl;
            }
            break;
        case 3:
            cout<<"\nVuelva pronto!"<<endl; break;
        default: 
            cout<<"\nOperacion invalida"<<endl;
    }

    return 0;
}