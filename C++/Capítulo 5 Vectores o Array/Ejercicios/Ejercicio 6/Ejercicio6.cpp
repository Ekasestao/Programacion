#include<iostream>
#include<stdlib.h>

using namespace std;

int main()
{
    int numeros[5] = {1, 2, 10, 3, 4}, suma = 0, mayor = 0;

    for (int i = 0; i < 5; i++)
    {
        suma += numeros[i];

        if (numeros[i] > mayor)
        {
            mayor = numeros[i];
        }
    }

    if (mayor == suma - mayor)
    {
        cout<<"Si"<<endl;
    }
    else 
    {
        cout<<"No"<<endl;
    }


    system("pause");
    return 0;
}