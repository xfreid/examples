#include "Polar.h"
#include <iostream>
#include <sstream>
#include <math.h>


Polar::Polar(double radius, double angle)
  : m_radius (radius), m_angle (angle)
{}

std::string Polar::ToString() {
    std::stringstream ss;
    ss << "(" << m_radius << " ," << m_angle << ")";
    return ss.str();
}

double Polar::Distance(const Polar& coord) {
    // law of cosine
    double dist = std::sqrt((m_radius * m_radius) + (coord.m_radius * coord.m_radius)
                  - 2 * m_radius * coord.m_radius * cos ( coord.m_angle - m_angle ));
    return dist;
}

