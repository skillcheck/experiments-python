import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *

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

'''
Presents a GUI that calculates the average from a list of numbers entered by
the user.
'''
class Averager(QMainWindow):

    def __init__(self):
        super(Averager, self).__init__()
        self.initUI()

    def initUI(self):
        cw = QWidget(self)
        self.setCentralWidget(cw)

        gl = QGridLayout(cw)

        label1 = QLabel("Enter values: ", cw, alignment=Qt.AlignCenter)
        gl.addWidget(label1, 0, 0)

        self.lineEdit = QLineEdit(cw)
        gl.addWidget(self.lineEdit, 0, 1)
        self.lineEdit.editingFinished.connect(self.inputEdited)

        label2 = QLabel("The Average is: ", cw, alignment=Qt.AlignRight)
        gl.addWidget(label2, 1, 0)

        self.result = QLineEdit(cw)
        gl.addWidget(self.result, 1, 1)
        self.result.setReadOnly( True )

    def inputEdited(self):
        values = self.sender().text().split(',')
        self.result.setText(str(calculateAverage(values)))

def main():
    app = QApplication(sys.argv)

    averager = Averager()

    averager.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
