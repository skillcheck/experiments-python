from PySide6.QtOpenGL import QOpenGLFunctions_1_3
from PySide6.QtOpenGLWidgets import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

from OpenGL.GL import *
from OpenGL.GLU import *

import sys

class GLWidget(QOpenGLWidget):

    def __init__(self, parent):
        super(GLWidget, self).__init__(parent)

    def minimumSizeHint(self):
        return QSize(100, 300)

    def sizeHint(self):
        return QSize(400, 400)

    def initializeGL(self):
        super().initializeGL()
        # Set up the rendering context, define display lists etc.:
        glClearColor( 1.0, 0.0, 0.0, 1.0 )
        glEnable(GL_DEPTH_TEST)

    def resizeGL(self, w, h):
        # setup viewport, projection etc.:
        glViewport(0, 0, w, h)

    def paintGL(self):
        # draw the scene:
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glColor3f(1,0,0)
        glRectf(-1,-1,1,0)
        glColor3f(0,1,0)
        glRectf(-1,0,1,1)
        glBegin(GL_TRIANGLES)
        glVertex2f(3.0, 3.0)
        glVertex2f(5.0, 3.0)
        glVertex2f(5.0, 5.0)
        glVertex2f(6.0, 4.0)
        glVertex2f(7.0, 4.0)
        glVertex2f(7.0, 7.0)
        glEnd()
        glFinish()


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

    glw = GLWidget(cw)
    layout.addWidget(glw, row, 0, 1, 2)
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
