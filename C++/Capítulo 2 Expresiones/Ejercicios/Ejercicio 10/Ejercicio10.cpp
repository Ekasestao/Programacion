#include<iostream>
#include<math.h>

using namespace std;

int main(){
    float a,b,c,resultado=0,resultado2=0;

    cout<<"Introduzca el valor de a: "; cin>>a;
    cout<<"Introduzca el valor de b: "; cin>>b;
    cout<<"Introduzca el valor de c: "; cin>>c;

    resultado=(-b+(sqrt(pow(b,2)-(4*a*c))))/(2*a);
    resultado2=(-b-(sqrt(pow(b,2)-(4*a*c))))/(2*a);

    cout.precision(2);
    cout<<"\nEl primer resultado es de:"<<resultado<<endl;
    cout<<"\nEl segundo resultado es de:"<<resultado2<<endl;

    return 0;
}