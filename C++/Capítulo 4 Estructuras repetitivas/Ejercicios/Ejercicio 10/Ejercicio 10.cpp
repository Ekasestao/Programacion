#include<iostream>
#include<stdlib.h>

using namespace std;

int main()
{
    int n, fact = 1, suma = 0;

    cout<<"Digite n: "; cin>>n;

    for (int i = 1; i<=n; i++)
    {
        fact *= i;
        suma += fact;
    }

    cout<<"\nEl resultado es: "<<suma<<endl;

    system("pause");
    return 0;
}