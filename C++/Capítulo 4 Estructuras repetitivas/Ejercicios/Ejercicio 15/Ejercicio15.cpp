#include<iostream>
#include<stdlib.h>
#include<time.h>

using namespace std;

int main()
{
    int n, na, contador = 0;

    srand(time(NULL));
    na = rand()%(101);

    do
    {
        cout<<"Digite un numero: "; cin>>n;

        if (n<na)
        {
            cout<<"El numero es mayor"<<endl;
            contador ++;
        }
        if (n>na)
        {
            cout<<"El numero es menor"<<endl;
            contador ++;
        }
    } while (na != n);

    cout<<"\nAcertaste el numero "<<na<<" en "<<contador<<" intentos"<<endl;

    system("pause");
    return 0;
}