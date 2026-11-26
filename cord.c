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
    double dd1 = floor(dd1);
    double dd2 = floor(dd2);

    if (d1<0 && d2<0 || d1>0 && d2>0)
    int sign = 1;

    else
    int sign = -1;
    
    double *prod = dd1*dd2;
    
    double *sum = dd2+dd1;

    return (sign);
}
