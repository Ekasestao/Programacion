#include<iostream>

using namespace std;

int main(){
    int edad;

    cout<<"Digite su edad: "; cin>>edad;

    if ((edad>=18) && (edad<=25)){
        cout<<"Tu edad esta entre los 18 y los 25"<<endl;
    }
    else{
        cout<<"Tu edad no esta entre los 18 y los 25"<<endl;
    }

    return 0;
}