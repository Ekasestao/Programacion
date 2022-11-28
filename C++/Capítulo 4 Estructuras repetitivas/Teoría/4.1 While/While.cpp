#include<iostream>
#include<conio.h> 

using namespace std;

int main(){
    int i;

    i=10; //inicializar iterador antes del bucle while

    while (i>=1){
        cout<<i<<endl;
        i--; //i-- = i-=1 de Python
    }
    
    getch();
    return 0;
}