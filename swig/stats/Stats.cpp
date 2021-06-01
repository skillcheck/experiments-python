#include "Stats.hpp"

#include <numeric>

Stats::Stats() : mValues()
{
}

void
Stats::setValues( RealVec const & values )
{
  mValues = values;
}

Stats::RealVec const &
Stats::getValues() const
{
  return mValues;
}

Stats::Real
Stats::getMean() const
{
  if ( mValues.empty() ) {
    return 0.0;
  }
  Real sum =
      std::accumulate( mValues.begin(), mValues.end(), 0.0, std::plus<Real>() );
  return sum / mValues.size();
}
