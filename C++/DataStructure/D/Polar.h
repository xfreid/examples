
#ifndef POLAR_H_
#define POLAR_H_

#include "Coordinate.h"

class Polar : public Coordinate
{
  public:
    // angle in radians
    Polar(double radius, double angle);

    /*virtual*/ std::string ToString() override;
    double Distance (const Polar& coord);

  public:
    double m_radius, m_angle;
};

#endif