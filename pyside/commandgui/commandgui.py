from gui import CommandGUI

from PySide6.QtWidgets import *

import os
import subprocess
import sys

def runCommand(gui):
    '''
    Runs the command based on data from gui.
    See: https://stackoverflow.com/questions/4760215/running-shell-command-and-capturing-the-output
    '''
    command = gui.ui.commandEntry.currentText()
    workDir = gui.ui.workingDirectoryEntry.currentText()
    if not command or not workDir:
        return
    print('Running Command: ', command, ' in: ', workDir, flush=True)

    commandParams = command.split()
    origDir = os.getcwd()
    os.chdir(workDir)
    output = subprocess.run( commandParams,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        shell=True
    )
    # The command may have changed the current working directory, so retrieve
    # it again and update the GUI
    # Note: Child processes can't change parent process' cwd so this is not
    # really needed.
    workDir = os.getcwd()
    os.chdir(origDir)
    gui.appendOutput(output.stdout.decode("utf-8"))

def main():
    app = QApplication(sys.argv)

    gui = CommandGUI(None)
    gui.ui.commandRun.clicked.connect( lambda : runCommand(gui) )
    gui.ui.closeButton.clicked.connect(exit)

    gui.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

