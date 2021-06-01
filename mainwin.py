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

    mainwin.show();
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
