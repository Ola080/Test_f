#include <stdio.h>
#include <math.h>
#include <stdbool.h>

struct date
{
    int day;
    int month;
    int year;
};

bool leap(struct date *test_date)
{
    int year = test_date->year;
    return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
}

int count (struct date *test_date)
{
    static const int days_in_month[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int month = test_date->month;

    if (month < 1 || month > 12)
        return -1;

    if (month == 2 && leap(test_date))
        return 29;

    return days_in_month[month - 1];
}