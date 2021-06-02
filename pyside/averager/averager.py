from cesium.averager_gui import Averager
from PySide6.QtWidgets import *
import sys

def main():
    app = QApplication(sys.argv)

    averager = Averager()
    averager.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
