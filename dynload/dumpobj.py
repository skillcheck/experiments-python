import os.path, importlib
import inspect
import pkgutil

from pprint import pprint
import sys

def dumpPkg(inputName, indent = ''):
    print(indent, 'dumpPkg(', inputName,')')
    pkgpath = os.path.dirname(inputName)
    contents = [name for _, name, _ in pkgutil.iter_modules([inputName])]
    #print(indent + 'Contents:')
    #pprint(contents)
    
    for item in contents:
        dumpImport(inputName + '.' + item, indent+'  ')

def dumpImport(inputName, indent = ''):
    print(indent, 'dumpImport(', inputName,')')
    object = importlib.import_module(inputName)

    if inspect.ismodule(object):
        dumpPkg(inputName, indent)
    elif inspect.isclass(object):
        for name, obj in inspect.getmembers(object, inspect.isclass):
            print(indent, 'Class: ', name)

def main():

    print('Print Object to load:')
    inputName = input()
    
    dumpImport(inputName)
     
     
if __name__ == "__main__":
    main()