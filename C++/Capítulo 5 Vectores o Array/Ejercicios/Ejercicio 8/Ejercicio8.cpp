#include<iostream>
#include<stdlib.h>

using namespace std;

int main()
{
    int n, numeros[100], numeros2[100];

    cout<<"Digite el numero de elementos: "; cin>>n;

    for (int i = 0; i < n; i++)
    {
        cout<<i + 1<<". Digite un numero: "; cin>>numeros[i];
    }

    for (int i = 0; i < n; i++)
    {
        numeros2[i] = numeros[i] * 2;
    }

    for (int i = 0; i < n; i++)
    {
        cout<<numeros2[i]<<endl;
    }

    system("pause");
    return 0;
}