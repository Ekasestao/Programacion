#include<iostream>
#include<stdlib.h>

using namespace std;

int main()
{
    int numeros[100], n;

    cout<<"Digite el numero de elementos: "; cin>>n;

    for (int i = 0; i < n; i++)
    {
        cout<<"Digite un numero: "; cin>>numeros[i];
    }

    for (int i = 0; i < n; i++)
    {
        cout<<i<<" -> "<<numeros[i]<<endl;
    }

    system("pause");
    return 0;
}