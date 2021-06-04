from pprint import pprint
import importlib
from inspect import *

class ModuleTree:
  def __init__(self, obj, indent=''):
    self.isModule = ismodule(obj)
    #pprint(dir(obj))
    if ismodule(obj):
      pprint(indent+'Module: '+obj.__name__)
      for val in dir(obj):
        try:
          if ((val[0:2] == 'Py') or (val[0] == 'Q')):
            attr = getattr(obj, val)
            if isclass(attr):
              pprint(indent+'  Class: '+obj.__name__+'.'+attr.__name__)
            elif ismodule(attr):
              object = importlib.import_module(attr.__name__)
              ModuleTree(object, indent+'  ')

        except:
          pass

def main():

  module = importlib.import_module('importpyside6')
  pysideInfo = ModuleTree(module)

if __name__ == "__main__":
  main()
