#include<iostream>
#include<stdlib.h>

using namespace std;

int main()
{
    int n, fact = 1;

    cout<<"Digite n: "; cin>>n;

    for (int i = 1; i<=n; i++)
    {
        fact *= i;
    }

    cout<<"\nEl resultado es: "<<fact<<endl;

    system("pause");
    return 0;
}