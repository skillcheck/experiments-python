import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *

def main():
    app = QApplication(sys.argv)

    mainwin = QMainWindow()

    cw = QWidget( mainwin )
    mainwin.setCentralWidget( cw )

    gl = QGridLayout( cw )

    label = QLabel("Hello World", cw, alignment=Qt.AlignCenter)
    gl.addWidget( label, 0, 0 )

    lineEdit = QLineEdit( cw )
    gl.addWidget( lineEdit, 0, 1 )

    slider = QSlider( Qt.Horizontal, cw )
    gl.addWidget( slider, 1, 0, 1, 2 )

    slot = lambda value : lineEdit.setText( str(value) )
    slider.valueChanged.connect( slot )

    mainwin.show();
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
