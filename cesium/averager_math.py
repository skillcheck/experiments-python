from PySide6.QtWidgets import *

def calculateAverage(values):
    try:
        numValues = len(values)
        sum = 0
        for value in values:
            sum += float(value)

    except ValueError as err:
        QMessageBox.warning(None, "Value Error", "Value Error: {0}".format(err))
    except:
        QMessageBox.warning(None, "Exception", "Exception: {0}".sys.exc_info()[0])

    return sum / numValues

