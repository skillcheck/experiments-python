from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
import sys

def main():
    app = QApplication(sys.argv)

    mainWin = QMainWindow()

    # Create Menu
    menuBar = QMenuBar(mainWin)
    mainWin.setMenuBar(menuBar)

    fileMenu = menuBar.addMenu("File")
    newAction = fileMenu.addAction("New")
    openAction = fileMenu.addAction("Open")
    fileMenu.addSeparator()
    saveAction = fileMenu.addAction("Save")
    saveAsAction = fileMenu.addAction("Save As")
    saveAllAction = fileMenu.addAction("Save All")
    fileMenu.addSeparator()
    closeAction = fileMenu.addAction("Close")
    closeAllAction = fileMenu.addAction("Close All")
    fileMenu.addSeparator()
    exitAction = fileMenu.addAction("Exit")
    exitAction.triggered.connect(lambda : exit())

    # Create Central Widgets
    cw = QWidget(mainWin)
    mainWin.setCentralWidget(cw)

    layout = QGridLayout(cw)
    row = 0

    label = QLabel("Hello World", cw, alignment=Qt.AlignCenter)
    layout.addWidget(label, row, 0)

    lineEdit = QLineEdit(cw)
    layout.addWidget(lineEdit, row, 1)
    row += 1

    slider = QSlider(Qt.Horizontal, cw)
    layout.addWidget(slider, row, 0, 1, 2)
    row += 1

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
        layout.addWidget(ui, row, 0, 1, 2)
        uifile.close()
        ui.EuroSim_SimConfig_UserId_TextField.setText("1000")
        ui.EuroSim_SimConfig_Close_Button.clicked.connect(lambda : exit())

    mainWin.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
