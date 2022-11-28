#include<iostream>
#include<stdlib.h>

using namespace std;

int main()
{
    int numeros[2][2] = {{1, 2} , {3, 4}}, numeros2[2][2];

    for (int i = 0; i < 2; i++)
    {
        for (int e = 0; e < 2; e++)
        {
            cout<<numeros[i][e]<<" ";
        }
        cout<<"\n";
    }

    cout<<"\n";

    for (int i = 0; i < 2; i++)
    {
        for (int e = 0; e < 2; e++)
        {
            numeros2[i][e] = numeros[i][e];
        }
    }

    for (int i = 0; i < 2; i++)
    {
        for (int e = 0; e < 2; e++)
        {
            cout<<numeros2[i][e]<<" ";
        }
        cout<<"\n";
    }

    system("pause");
    return 0;
}