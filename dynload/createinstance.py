#import PySide6
#import PySide6.QtCore
#from PySide6.QtCore import *

import os, os.path, importlib
import inspect
import pkgutil

from pprint import pprint
import sys

def getClassObject(obj):

  if obj is None:
    while obj is None:
      print('Enter Module or Class to load, or empty to exit:')
      name = input()
      if not name:
        exit()

      try:
        obj = importlib.import_module(name)
        
      except Exception:
        obj = None

      if obj is None:
        print('Could not load module/class, try again...')

    return obj
    
  if inspect.isclass(obj):
    return obj
    
  # Select SubModule or Class
  classNames = list()
  moduleNames = list()
  #pprint(dir(obj))
  for name in dir(obj):
    attr = getattr(obj, name)
    if (inspect.isclass(attr)):
      classNames.append(name)
    elif (inspect.ismodule(attr)):
      moduleNames.append(name)

  print('SubModules:')
  pprint(moduleNames)
  print('Classes:')
  pprint(classNames)

  print('\nEnter the next part of the name, or empty to exit:')
  subName = input()
  if not subName:
    exit()

  newObj = None
  attr = getattr(obj, subName)
  if inspect.isclass(attr):
    className = obj.__name__+'.'+attr.__name__
    print('Instantiating class: '+className)

    #temp = __import__(obj.__name__, globals={"__name__":attr.__name__})
    #temp = __import__(obj.__name__, globals={"__name__":attr.__name__}, locals={}, level=3)
    temp = __import__(obj.__name__, globals(), locals(), level=3)

    print('Globals:')
    pprint(globals())
    klass = globals()[attr.__name__]
    newObj = klass()
    return newObj
  
  if inspect.ismodule(attr):
    try:
      newObj = importlib.import_module(attr.__name__)
    except Exception:
      print('Could not import module, Abortin... ')
      exit()

  print('Loaded new Module/Class: '+newObj.__name__)

  return newObj

def main():

  obj = None
  obj = getClassObject(obj)
  
  while not inspect.isclass(obj):
    obj = getClassObject(obj)

  print('Initiated class instance: '+obj.__name__)

if __name__ == "__main__":
  main()
