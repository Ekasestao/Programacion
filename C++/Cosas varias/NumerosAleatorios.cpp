#include<iostream>
#include<math.h>
#include<time.h>

int main()
{
    int n;

    srand(time(NULL));
    n = 1 + rand()%((100 + 1) - 1); //Número aleatorio = límite inf + rand()%((límite sup + 1) - límite inf) 

    return 0;
}