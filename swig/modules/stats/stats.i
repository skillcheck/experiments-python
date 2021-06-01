%module stats
%{
#include <stats/Stats.hpp>
%}

%include "std_vector.i"
%feature("valuewrapper") Stats;
%include <stats/Stats.hpp>
%naturalvar RealVec;
%template(RealVec) std::vector<double>;
%naturalvar;
