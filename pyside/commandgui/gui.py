from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

import os
import sys

def insertComboBoxEntry( comboBox, entry):
    '''
    Inserts entry at top of ComboBox list. If already exists, moves it to the
    top of the list. Sets the current index to the top of the list.
    '''
    if not entry:
        return
    index = comboBox.findText(entry)
    if index >= 0:
        comboBox.removeItem(index)
    comboBox.insertItem(0, entry)
    comboBox.setCurrentIndex(0)

class CommandGUI(QWidget):

    def __init__(self, parent):
        super(CommandGUI, self).__init__(parent)

        self.initGUI()

    def browseWorkingDir(self):
        dir = QFileDialog.getExistingDirectory(self,
            'Select Working Directory',
            self.ui.workingDirectoryEntry.currentText())
        insertComboBoxEntry(self.ui.workingDirectoryEntry, dir)

    def runCommand(self):
        insertComboBoxEntry(
            self.ui.commandEntry,
            self.ui.commandEntry.currentText())

    def insertCommand(self, command):
        if not command:
            return
        index = self.ui.commandEntry.findText(command)
        if index >= 0:
            self.ui.commandEntry.removeItem(index)
        self.ui.commandEntry.insertItem(0, command)
        self.ui.commandEntry.setCurrentIndex(0)

    def clearOutput(self):
        self.ui.outputText.clear()

    def copyOutput(self):
        output = self.ui.outputText.toPlainText()
        if output:
            clipboard = QGuiApplication.clipboard()
            clipboard.setText(output)

    def saveOutput(self):
        print('saveOutput()', flush=True)

    def appendOutput(self, output):
        if self.ui.outputAutoClear.isChecked():
            self.ui.outputText.clear()

        self.ui.outputText.moveCursor(QTextCursor.End)
        self.ui.outputText.insertPlainText(output)
        self.ui.outputText.moveCursor(QTextCursor.End)

    def initGUI(self):
        layout = QVBoxLayout(self)

        loader = QUiLoader()
        uifile = QFile('commandgui.ui')
        uifile.open(QFile.ReadOnly)
        self.ui = loader.load(uifile, self)
        layout.addWidget(self.ui)
        uifile.close()

        self.ui.workingDirectoryEntry.insertItem(0, os.getcwd())
        self.ui.commandEntry.insertItem(0, 'ls -al')

        self.ui.workingDirectoryBrowse.clicked.connect(self.browseWorkingDir)
        self.ui.commandRun.clicked.connect(self.runCommand)
        self.ui.outputClear.clicked.connect(self.clearOutput)
        self.ui.outputCopy.clicked.connect(self.copyOutput)
        self.ui.outputSave.clicked.connect(self.saveOutput)
