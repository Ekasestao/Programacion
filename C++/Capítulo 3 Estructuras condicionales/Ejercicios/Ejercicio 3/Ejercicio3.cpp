#include<iostream>

using namespace std;

int main(){
    int n;

    cout<<"Digite un numero entero: "; cin>>n;
    if (n==0){
        cout<<"El numero es cero";
    }
    else if (n%2==0){
        cout<<"El numero es par";
    }
    else {
        cout<<"El numero es impar";
    }

    return 0;
}