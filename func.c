#include <stdio.h>

void minfunction(int size, double values[])
{
    int min = 0
    for (int x=0; x<n;x++)
    {
        if min > values[x]
        min = values[x]
    }
    return min;


}

void stringconversion(int newsize, int size, char newarray[], char *array[])
{
    newarray[0] = '\0';
    int used = 0;
    for (int x = 0; x < size; x++)
    {
        int len = strlen(array[x]);
        if (used + len >= newsize)   // stop before overflowing newarray
            break;
        strcat(newarray, array[x]);
        used += len;
    }
}
