#include<iostream>

using namespace std;

int main(){
    int edad;
    char sexo[10]; //Indicamos que nuestra variable tipo char (caracter) tenga 10 caracteres como máximo
    float altura;

    cout<<"Digite su edad: "; cin>>edad;
    cout<<"Digite su sexo: "; cin>>sexo;
    cout<<"Digite su altura en metros: "; cin>>altura;
    
    cout<<edad<<endl;
    cout<<"\nSexo: "<<sexo<<endl;
    cout<<"\nAltura en metros: "<<altura<<endl;
    
    return 0;
}