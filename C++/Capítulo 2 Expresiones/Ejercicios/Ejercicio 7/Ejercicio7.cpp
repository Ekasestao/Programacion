#include<iostream>

using namespace std;

int main(){
    float a,b,c,media=0;

    cout<<"Ingrese su nota practica: "; cin>>a;
    cout<<"Ingrese su nota teorica: "; cin>>b;
    cout<<"Ingrese su nota participatoria: "; cin>>c;

    media=(a*0.3)+(b*0.6)+(c*0.1);

    cout.precision(2);
    cout<<"\nSu nota final es de: "<<media<<endl;

    return 0;
}