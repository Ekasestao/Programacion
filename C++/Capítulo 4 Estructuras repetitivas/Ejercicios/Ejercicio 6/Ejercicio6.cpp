#include<iostream>
#include<stdlib.h>

using namespace std;

int main()
{
    int x, y, mult = 1;

    cout<<"Introduzca el valor de x e y: "; cin>>x>>y;

    for (int i = 1; i <= y; i++)
    {
        mult *= x;
    }
    
    cout<<"\nEl resultado es: "<<mult<<endl;

    system("pause");
    return 0;
}