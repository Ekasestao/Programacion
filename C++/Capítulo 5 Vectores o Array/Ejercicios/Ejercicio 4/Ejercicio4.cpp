#include<iostream>
#include<stdlib.h>

using namespace std;

int main()
{
    int numeros[5] = {1, 2, 3, 4, 5};

    for (int i = 4; i >= 0; i--)
    {
        cout<<numeros[i]<<endl;
    }

    system("pause");
    return 0;
}