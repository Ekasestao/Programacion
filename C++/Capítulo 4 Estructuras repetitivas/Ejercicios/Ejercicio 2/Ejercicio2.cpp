#include<iostream>
#include<stdlib.h>

using namespace std;

int main()
{
    int n, s = 0;

    do
    {
        cout<<"Digite un numero: "; cin>>n;
        if (n > 0)
        {
            s++;
        }
    }
    while (n != 0);

    cout<<"El numero de valores mayores que cero son "<<s<<endl;

    system("pause");
    return 0;
}