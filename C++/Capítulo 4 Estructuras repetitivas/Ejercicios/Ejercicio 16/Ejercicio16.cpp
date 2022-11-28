#include<iostream>
#include<stdlib.h>

using namespace std;

int main()
{
    int n, resultado;

    cout<<"Digite un numero: "; cin>>n;

    for (int i = 2; n > 1; i++)
    {
        while (n % i == 0)
        {
            cout<<i<<" ";
            n /= i;
        }
        
    }

    cout<<endl;

    system("pause");
    return 0;
}