#include<iostream>
#include<stdlib.h>
#include<math.h>

using namespace std;

int main()
{
    int n, suma = 0;

    cout<<"Digite n: "; cin>>n;

    for (int i = 1; i <= n; i++)
    {
        suma += pow(2, i);
    }

    cout<<"\nEl resultado es: "<<suma<<endl;

    system("pause");
    return 0;
}