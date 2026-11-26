#include <stdio.h>
#include <string.h>
#include <math.h>

struct point{
    double x;
    double y;
};

double distance(struct point p1, struct point p2)
{
    double dx = p2.x - p1.x;
    double dy = p2.y - p1.y;
    return sqrt(dx * dx + dy * dy);
}



int analyse(double *prod, double *sum, double d1, double d2)
{
    double dd1 = floor(d1);
    double dd2 = floor(d2);
    int sign;

    if ((d1 < 0 && d2 < 0) || (d1 > 0 && d2 > 0))
        sign = 1;
    else
        sign = -1;

    *prod = dd1 * dd2;
    *sum  = dd1 + dd2;

    return sign;
}

