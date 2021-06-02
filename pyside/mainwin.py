from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
import sys

def main():
    app = QApplication(sys.argv)

    mainWin = QMainWindow()



    # Create Central Widgets
    cw = QWidget(mainWin)
    mainWin.setCentralWidget(cw)

    gl = QGridLayout(cw)

    label = QLabel("Hello World", cw, alignment=Qt.AlignCenter)
    gl.addWidget(label, 0, 0)

    lineEdit = QLineEdit(cw)
    gl.addWidget(lineEdit, 0, 1)

    slider = QSlider(Qt.Horizontal, cw)
    gl.addWidget(slider, 1, 0, 1, 2)

    # def slot( value ):
    #     lineEdit.setText( str(value) )
    #
    #slider.valueChanged.connect( slot )
    slider.valueChanged.connect(lambda value : lineEdit.setText(str(value)))

    # Load UI file
    if (len(sys.argv) > 1):
        loader = QUiLoader()
        uifile = QFile(sys.argv[1])
        uifile.open(QFile.ReadOnly)
        ui = loader.load(uifile, cw)
        gl.addWidget(ui, 2, 0, 1, 2)
        uifile.close()
        ui.EuroSim_SimConfig_UserId_TextField.setText("1000")
        ui.EuroSim_SimConfig_Close_Button.clicked.connect(lambda : exit())

    mainWin.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
