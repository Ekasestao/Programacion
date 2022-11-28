#include<iostream>
#include<stdlib.h>

using namespace std;

int main()
{
    char letras[] = {'a', 'b', 'c', 'd', 'e'}, letras2[] = {'f', 'g', 'h', 'i', 'j'}, juntos[10];

    for (int i = 0; i < 5; i++)
    {
        juntos[i] = letras[i];
    }

    for (int i = 5; i < 10; i++)
    {
        juntos[i] = letras2[i - 5];
    }

    for (int i = 0; i < 10; i++)
    {
        cout<<juntos[i]<<endl;
    }

    system("pause");
    return 0;
}