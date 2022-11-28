#include<iostream>
#include<stdlib.h>

using namespace std;

int main()
{
    int numeros[3][3] = {{1, 2, 3} , {4, 5, 6} , {7, 8, 9}};

    for (int i = 0; i < 3; i++)
    {
        for (int e = 0; e < 3; e++)
        {
            cout<<numeros[i][e]<<" ";
        }
        cout<<"\n";
    }

    cout<<"\n";

    for (int i = 0; i < 3; i++)
    {
        for (int e = 0; e < 3; e++)
        {
            if (i == e)
            {
                cout<<numeros[i][e]<<endl;
            }
        }
    }

    system("pause");
    return 0;
}