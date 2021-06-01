'''
Calculates the average of provided list of values.
'''
def calculateAverage(values):
    numValues = len(values)
    sum = 0
    for value in values:
        sum += float(value)

    return sum / numValues
