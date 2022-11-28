#include<iostream>

using namespace std;

int main(){
    int n,n2,n3,n4;

    cout<<"Digite tres numeros: "; cin>>n>>n2>>n3;

    cout<<"\nDigite el cuarto numero: "; cin>>n4;
    
    if ((n==n4) || (n2==n4) || (n3==n4)){
        cout<<"El numero coincide";
    }
    else{
        cout<<"El numero no coincide";
    }
    
    return 0;
}