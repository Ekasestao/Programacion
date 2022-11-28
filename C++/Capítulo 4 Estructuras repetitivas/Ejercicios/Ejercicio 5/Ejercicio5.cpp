#include<iostream>
#include<stdlib.h>

using namespace std;

int main()
{
    int n, suma = 0;
    do
    {
        cout<<"Introduzca un numero: "; cin>>n;
        if (n > 0)
        {
            suma += n;
        }
    } while (((n != 0) && (30 < n) || (n < 20)));
    
    cout<<"\nLa suma es "<<suma<<endl;

    system("pause");
    return 0;
}