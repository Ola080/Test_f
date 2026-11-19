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

#include <stdio.h>
#include <string.h>

void stringsort(size_t rows, size_t cols, char countries[rows][cols])
{
    char temp[cols];

    for (size_t i = 0; i + 1 < rows; i++) {
        for (size_t j = 0; j + 1 < rows - i; j++) {
            if (strcmp(countries[j], countries[j + 1]) > 0) {
                strcpy(temp, countries[j]);
                strcpy(countries[j], countries[j + 1]);
                strcpy(countries[j + 1], temp);
            }
        }
    }
}

void stringconversion(size_t rows, size_t cols,
                      size_t lengths[rows], char strings[rows][cols])
{
    for (size_t i = 0; i < rows; i++) {
        lengths[i] = strlen(strings[i]);
        printf("%zu\n", lengths[i]);
    }
}
