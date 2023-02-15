import os, json
from pathlib import Path
from args import generateArgs
# Globals
output = {}

def checkIfDirectoryExistAndCreated() :
    global output
    fileName = str(Path.home()) +'/hornet/saveData.json'
    if not os.path.exists(fileName) :
        os.system('cp ~/Desktop/work/epub/saveData.json ~/hornet/saveData.json')
        print('File created')
    elif not os.path.exists(str(Path.home()) + '/hornet') :
        os.system('mkdir ~/hornet/')
        print("directory created ok")
    else:
        print('All exist')
    output = generateArgs()

def saveBookInData(pathBook) :
    checkIfDirectoryExistAndCreated()
    os.chdir(str(Path.home()) + '/hornet')
    #fileSavedData = open('saveData.json')
    print(pathBook)
