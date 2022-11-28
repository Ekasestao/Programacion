#include<iostream>
#include<stdlib.h>

using namespace std;

int main()
{
    int n, suma = 0;

    cout<<"Digite el ultimo numero: "; cin>>n;

    for (int i = 1; i <= 2*n-1; i += 2)
    {
        suma += i;
    }

    cout<<"\nLa suma total es de: "<<suma<<endl;

    system("pause");
    return 0;
}