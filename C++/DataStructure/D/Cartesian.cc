#include "Cartesian.h"
#include <iostream>
#include <sstream>
#include <math.h>

Cartesian::Cartesian(double x, double y)
  : m_x (x), m_y (y)
{}

std::string Cartesian::ToString() {
    std::stringstream ss;
    ss << "(" << m_x << " ," << m_y << ")";
    return ss.str();
}

double Cartesian::Distance(const Cartesian& coord) {
    double dist = sqrt((m_x - coord.m_x) * (m_x - coord.m_x) + 
                       (m_y - coord.m_y) * (m_y - coord.m_y));
    return dist;
}

