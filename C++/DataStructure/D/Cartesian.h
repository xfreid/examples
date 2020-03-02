#ifndef CARTESIAN_H_
#define CARTESIAN_H_

#include "Coordinate.h"

class Cartesian : public Coordinate
{
  public:
    Cartesian(double x, double y);

    /*virtual*/ std::string ToString() override;
    double Distance (const Cartesian& coord);

  public:
    double m_x, m_y;
};

#endif