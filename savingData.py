import os, json
from pathlib import Path

def checkIfDirectoryExistAndCreated() :
    # global output
    fileName = str(Path.home()) +'/hornet/saveData.json'
    if not os.path.exists(fileName) :
        if not os.path.exists(str(Path.home()) + '/hornet') :
            os.system('mkdir ~/hornet/')
            print("directory created ok")
        os.system('cp ./saveData.json ~/hornet/saveData.json')
        print('File created')
    # elif not os.path.exists(str(Path.home()) + '/hornet') :
    else:
        print('All exist')

def saveNewBookInData(actualBook) :
    # checkIfDirectoryExistAndCreated()
    os.chdir(str(Path.home()) + '/hornet')
    with open('saveData.json', 'r') as fileSavedData :
        savedBooks = json.load(fileSavedData)

    if len(savedBooks) < 1 :
        savedBooks.append(actualBook)
                
    for book in savedBooks : 
        # Save new book
        if book['bookTitle'] != actualBook['bookTitle'] : 
            savedBooks.append(actualBook)
            break 
    with open('saveData.json', 'w+') as jsonFile: 
        jsonFile.write(json.dumps(savedBooks, indent=4))
        jsonFile.close()

def saveActualState(actualBook) :
    os.chdir(str(Path.home()) + '/hornet')
    with open('saveData.json', 'r') as fileSavedData :
        savedBooks = json.load(fileSavedData)
    for book in savedBooks :
        if book['bookTitle'] == actualBook['bookTitle'] :
            book['actualPage'] = actualBook['actualPage']
            break
    with open('saveData.json', 'w+') as jsonFile :
        jsonFile.write(json.dumps(savedBooks, indent=4))
        jsonFile.close()

def loadBookState(actualBook) :
    os.chdir(str(Path.home()) + '/hornet')
    with open('saveData.json', 'r') as fileSavedData :
        savedBooks = json.load(fileSavedData)
    for book in savedBooks :
        if book['bookPath'] == actualBook['bookPath'] :
            return book['actualPage']
        else :
            return 0
