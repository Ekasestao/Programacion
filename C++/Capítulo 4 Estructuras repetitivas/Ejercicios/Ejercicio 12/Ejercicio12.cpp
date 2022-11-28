#include<iostream>
#include<stdlib.h>

using namespace std;

int main()
{
    int n, suma = 0;

    cout<<"Digite el valor de n: "; cin>>n;

    for (int i = 1; i <= n; i++)
    {
        if (i % 2 == 0)
        {
            suma -= i;
        }
        else if (i % 2 != 0)
        {
            suma += i;
        }
    }

    cout<<"\nEl resultado es: "<<suma<<endl;

    system("pause");
    return 0;
}