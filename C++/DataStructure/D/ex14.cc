#include "Cartesian.h"
#include "Polar.h"
#include <iostream>

#define PI 3.14159265

int main(int argc, char const *argv[])
{
    Cartesian c1(3.0, 0);
    Cartesian c2(0, 4.0);
    double dis = c1.Distance(c2);
    std::cout << "the distance between c1 " << c1.ToString() << " and c2 " << 
              c2.ToString() << " is " << dis << std::endl;

    Polar p1(1.0, 0);
    Polar p2(1.0, PI/2);
    dis = p1.Distance(p2);
    std::cout << "the distance between p1 " << p1.ToString() << " and p2 " << 
              p2.ToString() << " is " << dis << std::endl;

    return 0;
}
