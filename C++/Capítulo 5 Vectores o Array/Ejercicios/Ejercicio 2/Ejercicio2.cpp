#include<iostream>
#include<stdlib.h>

using namespace std;

int main()
{
    int numeros[] = {2, 4, 5, 3, 6}, mult = 1;

    for (int i = 0; i<5; i++)
    {
        mult *= numeros[i];
    }

    cout<<mult<<endl;

    system("pause");
    return 0;
}