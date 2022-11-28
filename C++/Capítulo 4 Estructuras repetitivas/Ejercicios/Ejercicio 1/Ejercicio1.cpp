#include<iostream>
#include<stdlib.h>

using namespace std;

int main()
{
    int n;

    do
    {
        cout<<"Digite un numero del 1 al 10: "; cin>>n;
    }
    while ((n < 1) || (n > 10));

    for (int i = 1; i <= 20; i++)
    {
        cout<<n<<" * "<<i<<" = "<<n*i<<endl;
    }

    system("pause");
    return 0;
}