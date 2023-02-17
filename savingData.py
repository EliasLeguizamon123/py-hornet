import os, json, platform
from pathlib import Path

PLATFORM = platform.platform()
SAVE_PATH = f'{Path.home()}\hornet\\' if 'windows' in PLATFORM.lower() else f'{Path.home()}/hornet/'

def checkIfDirectoryExistAndCreated() :
    # global output
    fileName = SAVE_PATH + 'saveData.json'
    if not os.path.exists(fileName) :
        if not os.path.exists(SAVE_PATH) :
            os.system(f'mkdir {SAVE_PATH}')
            print("directory created ok")

        if 'windows' in PLATFORM.lower():
            os.system(f'copy .\saveData.json {SAVE_PATH}saveData.json')
        else:
            os.system(f'cp ./saveData.json {SAVE_PATH}saveData.json')

        print('File created')
    else:
        print('All exist')

def saveNewBookInData(actualBook) :
    # checkIfDirectoryExistAndCreated()
    os.chdir(SAVE_PATH)
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
    os.chdir(SAVE_PATH)
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
    os.chdir(SAVE_PATH)
    with open('saveData.json', 'r') as fileSavedData :
        savedBooks = json.load(fileSavedData)
    for book in savedBooks :
        if book['bookPath'] == actualBook['bookPath'] :
            return book['actualPage']
        else :
            return 0
