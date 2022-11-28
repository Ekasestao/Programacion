#include<iostream>
#include<stdlib.h>

using namespace std;

int main()
{
    float x, y, z;
    int ta = 0, ua = 0, ue = 0;
    
    for (int i = 1; i <= 5; i++)
    {
        cout<<i<<". Digite las notas de los examenes: "; cin>>x>>y>>z;
        cout<<"\n";
    
        if ((x >= 5) && (y >= 5) && (z >= 5))
        {
            ta++;
        }

        if ((x >= 5) || (y >= 5) || (z >= 5))
        {
            ua++;
        }
        if ((x < 5) && (y < 5) && (z >= 5))
        {
            ue++;
        }

    }

    cout<<"\nAlumnos que aprobaron todos: "<<ta<<endl;
    cout<<"\nAlumnos que aprobaron almenos uno: "<<ua<<endl;
    cout<<"\nAlumnos que aprobaron unicamente el ultimo examen: "<<ue<<endl;
    
    system("pause");
    return 0;
}