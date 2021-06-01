#pragma once

#include <vector>

class Stats
{
public:
  using Real    = double;
  using RealVec = std::vector<Real>;

  Stats();

  RealVec const & getValues() const;
  void            setValues( RealVec const & values );

  Real getMean() const;

private:
  RealVec mValues;
}; // class Stats
