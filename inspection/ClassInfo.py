import PySide6

from PySide6 import QtCore
from PySide6.QtCore import *

from PySide6 import QtGui
from PySide6.QtGui import *

from PySide6 import QtWidgets
from PySide6.QtWidgets import *

from pprint import pprint
import importlib
from inspect import *
import sys

class ModuleInfo:
    def __init__(self, obj, indent=''):
        self.isModule = ismodule(obj)
        #pprint(indent+obj.__name__+' ismodule: '+str(ismodule(obj)))
        #pprint(dir(obj))
        if ismodule(obj):
            pprint(indent+'Module: '+obj.__name__)
            for val in dir(obj):
                try:
                    if ((val[0:2] == 'Py') or (val[0] == 'Q')):
                      #print(indent+'Trying: '+obj.__name__+'.'+val)
                      attr = getattr(obj, val)
                      if isclass(attr):
                          pprint(indent+'  Class: '+obj.__name__+'.'+attr.__name__)
                      elif ismodule(attr):
                          object = importlib.import_module(attr.__name__)
                          ModuleInfo(object, indent+'  ')

                except:
                    pass

        #elif isclass(obj):
        #    pprint(obj.__name__+' isclass: '+str(isclass(obj)))

        #pprint(getclasstree(dir(obj)))


class ClassInfo:
    def __init__(self, obj):
        self.isModule = ismodule(obj)
        self.isClass = isclass(obj)
        pprint(vars(obj))
        if isclass(obj):
            self.classType = obj.__class__
        else:
            self.classType = None

def main():

    app = QApplication(sys.argv)
    mainWin = QMainWindow()

    #mainWinInfo = ClassInfo(mainWin)
    #pprint(vars(mainWinInfo))
    #print(mainWinInfo.classType)

    pysideInfo = ModuleInfo(PySide6)
    #qtwidgetsInfo = ModuleInfo(QtWidgets)
    #qtguiinfo = ModuleInfo(QtGui)
    #qtcoreinfo = ModuleInfo(QtCore)

if __name__ == "__main__":
    main()
