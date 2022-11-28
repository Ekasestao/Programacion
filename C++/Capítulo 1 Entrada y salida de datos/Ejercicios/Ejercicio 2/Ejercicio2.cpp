#include<iostream>

using namespace std;

int main(){
    float precio=0,iva=0;

    cout<<"Indique el precio de su compra: ";
    cin>>precio;

    iva=precio*1.21;

    cout<<"El precio total es de: "<<iva<<" euros"<<endl;

    return 0;
}