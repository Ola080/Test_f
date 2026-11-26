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


