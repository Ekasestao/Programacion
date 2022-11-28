#include<iostream>

using namespace std;

int main(){
    float n1,n2,suma=0,resta=0,mult=0,divis=0;
    
    cout<<"Introduzca el primer numero: "; cin>>n1;
    cout<<"Introduzca el segundo numero: "; cin>>n2;
    suma=n1+n2;
    resta=n1-n2;
    mult=n1*n2;
    divis=n1/n2;

    cout<<"\nLa suma es: "<<suma<<endl;
    cout<<"\nLa resta es: "<<resta<<endl;
    cout<<"\nLa multiplicacion es: "<<mult<<endl;
    cout<<"\nLa division es: "<<divis<<endl;

    return 0;
}