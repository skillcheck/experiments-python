import stats

test = stats.Stats()
values = stats.RealVec([1, 2, 3])
test.setValues( values )

print( "Values are: ", list( test.getValues() ) )
print( "Mean is: ", test.getMean() )
