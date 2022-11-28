#include<iostream>

using namespace std;

int main(){
    float a,b,c,media=0;

    cout<<"Ingrese la primera nota: "; cin>>a;
    cout<<"Ingrese la segunda nota: "; cin>>b;
    cout<<"Ingrese la tercera nota: "; cin>>c;

    media=(a+b+c)/3;

    cout.precision(2);
    cout<<"\nLa media final es de: "<<media<<endl;

    return 0;
}