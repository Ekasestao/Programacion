#include<iostream>

using namespace std;

int main(){
    int saldoi=1000,opcion;
    float ing,ret,saldo=0;

    cout<<"\t.:Menu BBVA:."<<endl; 
    cout<<"1.Ingresar dinero en cuenta"<<endl;
    cout<<"2.Retirar dinero de la cuenta"<<endl;
    cout<<"3.Salir"<<endl;
    cout<<"Opcion: "; cin>>opcion;

    switch (opcion){
        case 1:
            cout<<"\nDigite la cantidad de dinero a ingresar: "; cin>>ing;
            saldo=saldoi+ing;
            cout<<"\nSu saldo es de: "<<saldo<<endl; break;
        case 2:
            cout<<"\nDigite la cantidad de dinero a retirar: "; cin>>ret;
            
            if (ret>saldoi){
                cout<<"\nNo tiene suficiente dinero"<<endl;
            }
            else{
                saldo=saldoi-ret;
                cout<<"\nSu saldo es de: "<<saldo<<endl; break;
            }

        case 3:
            cout<<"\nVuelva pronto!"<<endl; break;
    }

    return 0;
}