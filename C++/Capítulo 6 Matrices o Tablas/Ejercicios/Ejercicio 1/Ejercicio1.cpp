#include<iostream>
#include<stdlib.h>

using namespace std;

int main()
{
    int numeros[100][100], filas, columnas;

    cout<<"Digite filas: "; cin>>filas;
    cout<<"Digite columnas: "; cin>>columnas;

    for (int i = 0; i < filas; i++)
    {
        for (int e = 0; e < columnas; e++)
        {
            cout<<"Digite un numero ["<<i<<"]["<<e<<"]: "; cin>> numeros[i][e];
        }
    }

    for (int i = 0; i < filas; i++)
    {
        for (int e = 0; e < columnas; e++)
        {
            cout<<numeros[i][e];
        }
        cout<<"\n";
    }

    system("pause");
    return 0;
}