from PySide6.QtOpenGL import QOpenGLFunctions_1_3
from PySide6.QtOpenGLWidgets import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.arrays import vbo

import numpy as np
import sys

class GLWidget(QOpenGLWidget):

    def __init__(self, parent):
        super(GLWidget, self).__init__(parent)
        self.frameCount = 0

    def minimumSizeHint(self):
        return QSize(100, 300)

    def sizeHint(self):
        return QSize(400, 400)

    def initializeGL(self):
        super().initializeGL()
        # Set up the rendering context, define display lists etc.:
        glClearColor(0.0, 0.0, 0.5, 1.0)
        glEnable(GL_DEPTH_TEST)

        self.initGeometry()

        self.rotX = 0.0
        self.rotY = 0.0
        self.rotZ = 0.0

    def resizeGL(self, width, height):
        # setup viewport, projection etc.:
        glViewport(0, 0, width, height)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        aspect = width / float(height)

        gluPerspective(45.0, aspect, 1.0, 100.0)
        glMatrixMode(GL_MODELVIEW)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()    # push the current matrix to the current stack

        glTranslate(0.0, 0.0, -50.0) # third, translate cube to specified depth
        glScale(20.0, 20.0, 20.0)    # second, scale cube
        glRotate(self.rotX, 1.0, 0.0, 0.0)
        glRotate(self.rotY, 0.0, 1.0, 0.0)
        glRotate(self.rotZ, 0.0, 0.0, 1.0)
        glTranslate(-0.5, -0.5, -0.5) # first, translate cube center to origin

        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_COLOR_ARRAY)

        glVertexPointer(3, GL_FLOAT, 0, self.vertVBO)
        glColorPointer(3, GL_FLOAT, 0, self.colorVBO)

        if (self.cubeIdxArray is not None) and (len(self.cubeIdxArray) > 0):
            if self.cubeIdxArray.dtype == np.uint8:
                dtype = GL_UNSIGNED_BYTE
            elif self.cubeIdxArray.dtype == np.uint16:
                dtype = GL_UNSIGNED_SHORT
            else:
                dtype = GL_UNSIGNED_INT

            if self.frameCount == 0:
                glDrawElements(
                    GL_QUADS, len(self.cubeIdxArray),
                    dtype, self.cubeIdxArray)

        glDisableClientState(GL_VERTEX_ARRAY)
        glDisableClientState(GL_COLOR_ARRAY)

        glPopMatrix()    # restore the previous modelview matrix

        self.frameCount += 1

    def initGeometry(self):
        self.cubeVtxArray = np.array([[0.0, 0.0, 0.0],
                 [1.0, 0.0, 0.0],
                 [1.0, 1.0, 0.0],
                 [0.0, 1.0, 0.0],
                 [0.0, 0.0, 1.0],
                 [1.0, 0.0, 1.0],
                 [1.0, 1.0, 1.0],
                 [0.0, 1.0, 1.0]])
        self.vertVBO = vbo.VBO(np.reshape(self.cubeVtxArray,
                                          (1, -1)).astype(np.float32))
        self.vertVBO.bind()

        self.cubeClrArray = np.array([[0.0, 0.0, 0.0],
                 [1.0, 0.0, 0.0],
                 [1.0, 1.0, 0.0],
                 [0.0, 1.0, 0.0],
                 [0.0, 0.0, 1.0],
                 [1.0, 0.0, 1.0],
                 [1.0, 1.0, 1.0],
                 [0.0, 1.0, 1.0]])
        self.colorVBO = vbo.VBO(np.reshape(self.cubeClrArray,
                                           (1, -1)).astype(np.float32))
        self.colorVBO.bind()

        self.cubeIdxArray = np.array([0, 1, 2, 3,
                 3, 2, 6, 7,
                 1, 0, 4, 5,
                 2, 1, 5, 6,
                 0, 3, 7, 4,
                 7, 6, 5, 4], dtype=np.uint32)

    def setRotX(self, val):
        self.rotX = np.pi * val

    def setRotY(self, val):
        self.rotY = np.pi * val

    def setRotZ(self, val):
        self.rotZ = np.pi * val


def main():
    app = QApplication(sys.argv)

    mainWin = QMainWindow()
    mainWin.setWindowTitle('Python + Qt + OpenGL')

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

    # Make OpenGL-related stuff
    glw = GLWidget(cw)
    layout.addWidget(glw, row, 0, 1, 2)
    row += 1

    timer = QTimer(mainWin)
    timer.setInterval(20)   # period, in milliseconds
    timer.timeout.connect(glw.paintGL)
    timer.start()

    labelX = QLabel("X Rot: ")
    sliderX = QSlider(Qt.Horizontal)
    sliderX.valueChanged.connect(lambda val: glw.setRotX(val))
    layout.addWidget(labelX, row, 0)
    layout.addWidget(sliderX, row, 1)
    row += 1

    labelY = QLabel("Y Rot: ")
    sliderY = QSlider(Qt.Horizontal)
    sliderY.valueChanged.connect(lambda val: glw.setRotY(val))
    layout.addWidget(labelY, row, 0)
    layout.addWidget(sliderY, row, 1)
    row += 1

    labelZ = QLabel("Z Rot: ")
    sliderZ = QSlider(Qt.Horizontal)
    sliderZ.valueChanged.connect(lambda val: glw.setRotZ(val))
    layout.addWidget(labelZ, row, 0)
    layout.addWidget(sliderZ, row, 1)
    row += 1

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
