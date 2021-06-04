import os.path, importlib
import inspect
import pkgutil

from pprint import pprint
import sys

def dumpClasses(object, ind=''):
    for name, obj in inspect.getmembers(object, inspect.isclass):
        pprint(ind+'Class: '+name)


def dumpPkg(inputName, ind=''):
    pprint(ind+'dumpPkg('+inputName+')')
    pkgpath = os.path.dirname(inputName)
    contents = [name for _, name, _ in pkgutil.iter_modules([inputName])]
    
    if len(contents) > 0:
        pprint(ind+'Contents: '+str(contents))
        for item in contents:
            dumpImport(inputName + '.' + item, ind+'  ')
    else:
        object = importlib.import_module(inputName)
        dumpClasses(object, ind+'  ')

def dumpImport(inputName, ind = ''):
    pprint(ind+'dumpImport('+inputName+')')
    object = importlib.import_module(inputName)

    #pprint(ind+'ismodule: '+str(inspect.ismodule(object)))
    #pprint(ind+'isclass: '+str(inspect.isclass(object)))

    if inspect.ismodule(object):
        dumpPkg(inputName, ind+'  ')
    elif inspect.isclass(object):
        dumpClasses(object, ind+'  ')

def main():

    print('Print Object to load:')
    inputName = input()

    dumpImport(inputName)

if __name__ == "__main__":
    main()