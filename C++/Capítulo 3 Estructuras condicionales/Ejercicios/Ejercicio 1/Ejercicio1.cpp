#include<iostream>

using namespace std;

int main(){
    int n, n2;

    cout<<"Digite 2 numeros: "; cin>>n>>n2;

    if (n==n2){
        cout<<"Los numeros son iguales";
    }
    else if (n>n2){
        cout<<"El mayor es: "<<n;
    }
    else{
        cout<<"El mayor es: "<<n2;
    }

    return 0;
}
