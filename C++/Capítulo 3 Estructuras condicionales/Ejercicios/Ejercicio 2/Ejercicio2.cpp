#include<iostream>

using namespace std;

int main(){
    int n,n2,n3;

    cout<<"Digite 2 numeros: "; cin>>n>>n2>>n3;

    if ((n>=n2) && (n>=n3)){
        cout<<"El mayor es: "<<n;
    }
    else if ((n2>=n) && (n2>=n3)){
        cout<<"El mayor es: "<<n2;
    }
    else{
        cout<<"El mayor es: "<<n3;
    }

    return 0;
}
