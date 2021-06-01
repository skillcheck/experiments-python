from cesium.averager_gui import Averager
import sys
from PySide6.QtWidgets import *

def main():
    app = QApplication(sys.argv)

    averager = Averager()

    averager.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
