#include<iostream>
#include<stdlib.h>

using namespace std;

int main()
{
    float temperatura, sumatotal = 0, promedio = 0, mayor = 0, menor = 999;

    for (int i = 0; i < 24; i += 4)
    {
        cout<<"temperatura de la hora "<<i<<": "; cin>>temperatura;

        sumatotal += temperatura;

        if (temperatura > mayor)
        {
            mayor = temperatura;
        }
        if (temperatura < menor)
        {
            menor = temperatura;
        }
    }

    promedio = sumatotal / 6;

    cout<<"\nTemperatura Promedio: "<<promedio<<endl;
    cout<<"\nTemperatura más alta: "<<mayor<<endl;
    cout<<"\nTemperatura más baja: "<<menor<<endl;

    system("pause");
    return 0;
}