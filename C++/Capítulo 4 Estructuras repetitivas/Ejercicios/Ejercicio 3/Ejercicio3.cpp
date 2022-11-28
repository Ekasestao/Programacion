#include<iostream>
#include<stdlib.h>
#include<math.h>

using namespace std;

int main()
{
    int s = 0;

    for (int i = 1; i <= 10; i++)
    {
        s += pow(i, 2);
    }

    cout<<"La suma es "<<s<<endl;

    system("pause");
    return 0;
}