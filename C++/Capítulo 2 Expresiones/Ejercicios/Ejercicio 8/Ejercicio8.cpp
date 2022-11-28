#include<iostream>
#include<math.h> //Módulo math

using namespace std;

int main(){
    float a,b,c;

    cout<<"Digite el primer cateto: "; cin>>a;
    cout<<"Digite el segundo cateto: "; cin>>b;

    c=sqrt(pow(a,2)+pow(b,2)); //Pow para elevar a n una variable o valor

    cout.precision(2);
    cout<<"El valor de la hipotenusa es: "<<c<<endl;

    return 0;
}