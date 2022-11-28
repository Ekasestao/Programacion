#include<iostream>
#include<stdlib.h>

using namespace std;

int main()
{
    int numeros[] = {1, 2, 3, 4, 5}, suma = 0;

    for (int i = 0; i < 5; i++)
    {
        suma += numeros[i];
    }

    cout<<suma<<endl;

    system("pause");
    return 0;
}